# Contributing to marble-carver

Thank you for your interest in contributing. This project is built around a
simple but demanding philosophy:

> **Research is subtractive.** The truth already exists in the marble. Our job
> is to carve away everything that isn't it.

Every contribution — whether a template, a tool, a fix, or a piece of
documentation — should reinforce that idea.

---

## Principles

1. **Failures are first-class citizens.** Never discard a wrong path. Always
   document it so others don't walk it again.
2. **Retractions preserve the original.** When a claim is corrected, the
   original text stays visible. A dated audit note is added beside it.
3. **Transparency by default.** Every assumption, every citation, every dead
   end should be recorded.
4. **Mix modes.** Formal (Lean), empirical (mechanisms), and philosophical
   work all live here. Don't silo them.
5. **Solo → team → AI.** The workflow should work for one person, a
   human+AI pair, or a multi-agent swarm.

---

## How to contribute

### Bugs and feature requests

Open an issue using the provided templates. If you're reporting a broken
workflow, include the steps to reproduce.

### Templates

Templates are the heart of the project. Before proposing a change, study the
existing templates in `templates/` and the examples in `examples/`. Every
template must:

- Have a clear, single purpose.
- Include placeholder text that teaches the philosophy.
- Be valid Markdown.

### Python tooling

- Format with `ruff` (`ruff check . && ruff format .`).
- Target Python ≥ 3.10.
- Keep optional dependencies optional. The TUI must never be required.

### Documentation

Docs live in `docs/`. They should be:

- Clear enough for first-time researchers.
- Short enough to read in one sitting.
- Correct in every detail.

### Lean 4 / mathlib

Lean templates live in `math/`. They must:

- Build with `lake build` out of the box.
- Include `sorry` examples to demonstrate the carving workflow.
- Have audit notes in a visible `AuditNotes/` directory.

---

## Code of Conduct

All participants agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
Be generous with credit, specific with critique, and kind always.

---

## Getting started

```bash
git clone https://github.com/your-org/marble-carver.git
cd marble-carver

# Install core tools (no TUI)
pip install -e .

# Install with TUI
pip install -e ".[tui]"
```

Then look at `examples/` to see how a carving project is structured, and
read `docs/GETTING_STARTED.md`.
