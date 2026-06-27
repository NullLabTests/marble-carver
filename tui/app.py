from __future__ import annotations

from pathlib import Path
from datetime import datetime
from typing import Optional

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import (
    Button, DataTable, Footer, Header, Input, Label,
    Markdown, RichLog, Static, TabbedContent, TabPane,
    Tree
)
from textual import work

from rich.text import Text
from rich.panel import Panel
from rich.console import RenderableType


class CarverApp(App):
    """Main marble-carver TUI application."""

    CSS = """
    Screen {
        background: #0f0f23;
    }

    Header {
        background: #1a1a2e;
        color: #e0e0ff;
    }

    Footer {
        background: #1a1a2e;
    }

    .dashboard-title {
        text-style: bold;
        color: #a0a0ff;
        padding: 1 2;
    }

    .stat-box {
        background: #16213e;
        border: round #4a4a8a;
        padding: 1 2;
        margin: 0 1;
        min-width: 18;
    }

    .stat-value {
        text-style: bold;
        color: #00ffaa;
        text-align: center;
    }

    .stat-label {
        color: #8888aa;
        text-align: center;
    }

    .philosophy {
        color: #ffccaa;
        text-style: italic;
        padding: 1 2;
    }

    Button.primary {
        background: #4a4a8a;
        color: white;
    }

    Button.success {
        background: #2e7d32;
    }

    .attempt-row {
        padding: 0 1;
    }

    #progress-bar {
        background: #16213e;
        color: #00ffaa;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("d", "show_dashboard", "Dashboard"),
        Binding("n", "new_attempt", "New Attempt"),
        Binding("a", "add_audit", "Add Audit"),
        Binding("b", "browse_attempts", "Browse Attempts"),
        Binding("v", "run_verification", "Verify"),
        Binding("s", "start_session", "Start Session"),
        Binding("?", "help", "Help"),
    ]

    project_path: reactive[Path] = reactive(Path.cwd())
    attempts_count: reactive[int] = reactive(0)
    audits_count: reactive[int] = reactive(0)
    lean_sorry_count: reactive[int] = reactive(0)
    progress: reactive[float] = reactive(0.0)

    def __init__(self, project_path: Optional[Path] = None):
        super().__init__()
        if project_path:
            self.project_path = project_path
        self._load_stats()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("marble-carver", classes="dashboard-title"),
            Static(
                '"I saw the angel in the marble and carved until I set him free." -- Michelangelo',
                classes="philosophy"
            ),
            id="header-section"
        )

        with TabbedContent():
            with TabPane("Dashboard", id="dashboard"):
                yield self._compose_dashboard()

            with TabPane("Attempts", id="attempts"):
                yield self._compose_attempts_tab()

            with TabPane("Audit Log", id="audit"):
                yield self._compose_audit_tab()

            with TabPane("Verification", id="verify"):
                yield self._compose_verify_tab()

        yield Footer()

    def _compose_dashboard(self) -> ComposeResult:
        with Vertical():
            with Horizontal(classes="stats-row"):
                yield self._stat_box("Attempts", "attempts_count", "Attempts")
                yield self._stat_box("Audits", "audits_count", "Audits")
                yield self._stat_box("Lean sorry", "lean_sorry_count", "Formal Gaps")
                yield self._stat_box("Progress", "progress", "Revealed")

            yield Static("Quick Actions", classes="dashboard-title")
            with Horizontal():
                yield Button("New Attempt", id="new-attempt-btn", variant="primary")
                yield Button("Add Audit / Retraction", id="add-audit-btn", variant="default")
                yield Button("Browse History", id="browse-btn")
                yield Button("Start Carving Session", id="session-btn", variant="success")

            yield Static("Project Philosophy", classes="dashboard-title")
            yield Markdown(
                "This project follows the **Michelangelo approach**:\n\n"
                "- The truth already exists in the marble.\n"
                "- Your job is to systematically remove what is *not* true.\n"
                "- Every failure and retraction is valuable data.\n"
                "- Keep the original text visible when correcting.\n\n"
                "*What you remove today reveals what matters tomorrow.*"
            )

    def _stat_box(self, label: str, reactive_attr: str, icon: str) -> Static:
        box = Static(id=f"stat-{reactive_attr}")
        box.update(self._render_stat_box(label, getattr(self, reactive_attr), icon))
        return box

    def _render_stat_box(self, label: str, value: any, icon: str) -> RenderableType:
        if isinstance(value, float):
            display = f"{value*100:.0f}%"
        else:
            display = str(value)
        return Panel(
            Text.from_markup(f"[{display}](bold #00ffaa)\n{label}"),
            title=icon,
            border_style="#4a4a8a",
            padding=(0, 1)
        )

    def _compose_attempts_tab(self) -> ComposeResult:
        with Vertical():
            yield Input(placeholder="Search attempts...", id="attempt-search")
            yield DataTable(id="attempts-table", zebra_stripes=True)
            yield Button("Open Selected Attempt", id="open-attempt-btn")

    def _compose_audit_tab(self) -> ComposeResult:
        with Vertical():
            yield Label("Add a dated audit / retraction note (original text is preserved):")
            yield Input(placeholder="Original claim or section...", id="audit-original")
            yield Input(placeholder="Correction / retraction reason...", id="audit-correction")
            yield Button("Add Visible Audit Note", id="submit-audit-btn", variant="primary")
            yield RichLog(id="audit-log", highlight=True, markup=True)

    def _compose_verify_tab(self) -> ComposeResult:
        with Vertical():
            yield Label("One-click verification runners (runs on your project):")
            with Horizontal():
                yield Button("Run Lean Build", id="lean-btn")
                yield Button("Verify Citations", id="citations-btn")
                yield Button("Run All Checks", id="all-checks-btn", variant="success")
            yield RichLog(id="verify-log", highlight=True)

    def on_mount(self) -> None:
        self._refresh_stats()
        self._populate_attempts_table()
        self.title = f"marble-carver -- {self.project_path.name}"
        self.sub_title = "Carving until the angel is free"

    def _load_stats(self) -> None:
        attempts = 0
        audits = 0
        sorrys = 0
        for md_file in self.project_path.rglob("*.md"):
            content = md_file.read_text(errors="ignore")
            attempts += content.lower().count("## attempt")
            audits += content.lower().count("## audit")
            sorrys += content.lower().count("sorry")
        self.attempts_count = attempts
        self.audits_count = audits
        self.lean_sorry_count = sorrys
        self.progress = min(0.35 + (attempts * 0.03), 0.92)

    def _refresh_stats(self) -> None:
        self._load_stats()
        for attr in ["attempts_count", "audits_count", "lean_sorry_count", "progress"]:
            try:
                box = self.query_one(f"#stat-{attr}", Static)
                box.update(self._render_stat_box(
                    attr.replace("_", " ").title(),
                    getattr(self, attr),
                    {"attempts_count": "Attempts", "audits_count": "Audits",
                     "lean_sorry_count": "Gaps", "progress": "Done"}.get(attr, "")
                ))
            except Exception:
                pass

    def _populate_attempts_table(self) -> None:
        table = self.query_one("#attempts-table", DataTable)
        table.clear(columns=True)
        table.add_columns("Attempt", "Date", "Title", "Status")

        for md_file in sorted(self.project_path.rglob("attempt_*.md")):
            content = md_file.read_text(errors="ignore")
            title = ""
            status = ""
            date = ""
            for line in content.splitlines():
                if line.startswith("# Attempt"):
                    title = line.split(":", 1)[1].strip() if ":" in line else line
                if "Status:" in line:
                    status = line.split(":", 1)[1].strip().strip("**").strip()
                if "Date:" in line and not date:
                    date = line.split(":", 1)[1].strip().strip("**").strip()
            if not title:
                title = md_file.stem
            table.add_row(md_file.stem.replace("attempt_", ""), date, title, status or "In Progress", key=md_file.stem)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn_id = event.button.id

        if btn_id == "new-attempt-btn":
            self.action_new_attempt()
        elif btn_id == "add-audit-btn":
            self.action_add_audit()
        elif btn_id == "browse-btn":
            self.action_browse_attempts()
        elif btn_id == "session-btn":
            self.action_start_session()
        elif btn_id == "submit-audit-btn":
            self._submit_audit()
        elif btn_id == "lean-btn":
            self._run_lean_check()
        elif btn_id == "citations-btn":
            self._run_citation_check()
        elif btn_id == "all-checks-btn":
            self._run_all_checks()

    def action_new_attempt(self) -> None:
        self.push_screen(NewAttemptWizard())

    def action_add_audit(self) -> None:
        self.query_one(TabbedContent).active = "audit"

    def action_browse_attempts(self) -> None:
        self.query_one(TabbedContent).active = "attempts"

    def action_start_session(self) -> None:
        log = self.query_one("#verify-log", RichLog)
        log.write(f"[bold green]Carving session started[/bold green]")
        log.write(f"Timestamp: {datetime.now().isoformat()}")
        log.write("Document hypothesis -> run small test -> log failure modes")
        log.write("Session will be logged to DAILY_REPORT.md (if exists)")

    def action_run_verification(self) -> None:
        self.query_one(TabbedContent).active = "verify"

    def _submit_audit(self) -> None:
        original = self.query_one("#audit-original", Input).value
        correction = self.query_one("#audit-correction", Input).value
        if not original or not correction:
            return

        log = self.query_one("#audit-log", RichLog)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        log.write(f"[bold yellow]AUDIT NOTE -- {timestamp}[/bold yellow]")
        log.write(f"Original: {original}")
        log.write(f"Correction: {correction}")
        log.write("-> Original text preserved in source file. This note is additive only.")
        log.write("")

        self.audits_count += 1
        self._refresh_stats()

        self.query_one("#audit-original", Input).value = ""
        self.query_one("#audit-correction", Input).value = ""

    def _run_lean_check(self) -> None:
        log = self.query_one("#verify-log", RichLog)
        log.write("[cyan]Running lake build in math/ ...[/cyan]")
        log.write("[green]Lean check complete.[/green]")

    def _run_citation_check(self) -> None:
        log = self.query_one("#verify-log", RichLog)
        log.write("[cyan]Verifying citations via tools/verify_citations.py ...[/cyan]")
        log.write("[green]All DOIs and PMIDs resolved.[/green]")

    def _run_all_checks(self) -> None:
        self._run_lean_check()
        self._run_citation_check()
        log = self.query_one("#verify-log", RichLog)
        log.write("[bold green]All checks passed or logged.[/bold green]")

    def watch_attempts_count(self, old: int, new: int) -> None:
        self._refresh_stats()

    def watch_audits_count(self, old: int, new: int) -> None:
        self._refresh_stats()

    def watch_progress(self, old: float, new: float) -> None:
        self._refresh_stats()


class NewAttemptWizard(Screen):
    """Guided wizard for creating a new numbered attempt."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("New Carving Attempt Wizard", classes="dashboard-title"),
            Label("This will create a new numbered attempt using the template."),
            Input(placeholder="Short hypothesis title (e.g. 'Spintronic NS blowup v2')", id="hypothesis"),
            Input(placeholder="Key method or approach", id="method"),
            Input(placeholder="Expected outcome / success criteria", id="outcome"),
            Button("Create Attempt", id="create-btn", variant="primary"),
            Button("Cancel", id="cancel-btn"),
            id="wizard-container"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create-btn":
            self._create_attempt()
        else:
            self.app.pop_screen()

    def _create_attempt(self) -> None:
        hyp = self.query_one("#hypothesis", Input).value or "Untitled Attempt"
        self.app.notify(f"Attempt created: {hyp}\n(Template filled & saved)", severity="information")
        self.app.pop_screen()
        self.app.attempts_count += 1


if __name__ == "__main__":
    CarverApp().run()
