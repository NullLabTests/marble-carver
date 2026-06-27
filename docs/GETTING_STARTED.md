# Getting started

## 1. Clone or use as a template

**Option A: GitHub template**
Click "Use this template" on the repository page to create a new project
without the history.

**Option B: Clone the repo directly**

```bash
git clone https://github.com/your-org/marble-carver.git my-carving-project
cd my-carving-project
rm -rf .git && git init  # start fresh
```

## 2. Choose your setup

### Just the templates (no Python)

The `templates/` directory contains everything you need. Copy them into your
project and start writing Markdown. You don't need to install anything.

```bash
cp -r templates/ my-project/carvings/
```

### With Python helpers

```bash
pip install -e .
```

Then use the helper scripts:

```bash
# Add an audit note to an attempt
python tools/audit_helper.py --add carvings/attempt_001.md

# Verify citations in a project
python tools/verify_citations.py --check carvings/
```

### With the TUI

```bash
pip install -e ".[tui]"
marble-carver
```

The TUI will scan the current directory for carving projects and open a
dashboard.

## 3. Define your problem

Create a `problem_statement.md` using the template:

```bash
cp templates/problem_statement.md my-project/problem_statement.md
```

Describe the marble clearly. What is the angel you believe is inside?

## 4. Make your first attempt

```bash
cp templates/attempt.md my-project/carvings/attempt_001.md
```

Fill in:
- **Hypothesis** — What do you think is true?
- **Method** — How are you going to test it?
- **Results** — What happened?
- **Failures** — What went wrong? (This is valuable.)
- **Next steps** — What will you try next?

Commit it.

```bash
git add -A && git commit -m "attempt 001: initial hypothesis"
```

## 5. Document failures and audit

Found a mistake in a previous attempt? Don't edit it. Write an audit note:

```bash
cp templates/audit_note.md my-project/carvings/audit_001.md
```

This keeps the original claim visible and adds your correction beside it.

## 6. Track progress

Use the GitHub Projects board (suggested columns):

| Column | Meaning |
|--------|---------|
| **Marble Block** | Problems not yet touched |
| **Carving** | Active attempts |
| **Removed** | Falsified hypotheses (celebrated) |
| **Revealed** | Confirmed truths |

## 7. Use the TUI for daily work

```bash
marble-carver
```

From the dashboard you can:
- See attempt counts, audit counts, and Lean `sorry` counts
- Create new attempts with a guided wizard
- Browse and search all attempts
- Add audit notes
- Run verification scripts
- Log carving sessions

---

## Next steps

- Read `docs/WORKFLOW.md` for a detailed walkthrough.
- Explore the examples in `examples/`.
- If you're using Lean, look at `math/template/`.
