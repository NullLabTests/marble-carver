"""Command-line interface for marble-carver."""

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="marble-carver",
        description="Carve away everything that isn't the truth."
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version and exit.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    tui_parser = subparsers.add_parser("tui", help="Launch the interactive Textual TUI")
    tui_parser.add_argument(
        "--path", "-p",
        type=Path,
        default=Path.cwd(),
        help="Path to the carving project (default: current directory)"
    )

    init_parser = subparsers.add_parser(
        "init", help="Initialize a new carving project in current directory"
    )
    init_parser.add_argument(
        "--template", "-t",
        choices=["fundamental", "math", "mechanism"],
        default="fundamental",
        help="Which template to use"
    )

    verify_parser = subparsers.add_parser("verify", help="Run verification scripts")
    verify_parser.add_argument(
        "what",
        nargs="?",
        choices=["citations", "lean", "all"],
        default="all",
        help="What to verify"
    )

    args = parser.parse_args()

    if args.version:
        from marble_carver import __version__
        print(f"marble-carver v{__version__}")
        sys.exit(0)

    if args.command == "tui":
        try:
            from tui.app import CarverApp
            app = CarverApp(project_path=args.path)
            app.run()
        except ImportError:
            print("TUI dependencies not installed. Run: pip install -e .[tui]")
            sys.exit(1)
        except Exception as e:
            print(f"Error launching TUI: {e}")
            sys.exit(1)

    elif args.command == "init":
        print(f"Initializing new {args.template} carving project...")
        template_dir = Path(__file__).parent.parent / args.template / "template"
        if template_dir.exists():
            import shutil
            dest = Path.cwd() / args.template
            shutil.copytree(template_dir, dest, dirs_exist_ok=True)
            print(f"Created {dest / 'problem_statement.md'}")
        else:
            print(f"No template found for {args.template}. Creating minimal structure...")
            (Path.cwd() / args.template).mkdir(parents=True, exist_ok=True)
        print("Done. Start carving!")

    elif args.command == "verify":
        print(f"Running {args.what} verification...")
        if args.what in ("all", "citations"):
            from tools.verify_citations import check_file
            path = Path.cwd()
            files = list(path.rglob("*.md"))
            total, valid = 0, 0
            for f in files:
                results = check_file(str(f))
                if results:
                    total += len(results)
                    valid += sum(1 for r in results if r.get("valid"))
            print(f"  Citations: {valid}/{total} verified")
        if args.what in ("all", "lean"):
            print("  Lean: check manually with 'lake build' in math/")
        print("Verification complete.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
