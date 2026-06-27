# Workflow

## The carving cycle

```
                     ┌──────────────────┐
                     │  Problem defined  │
                     │  (the raw marble) │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  Propose attempt │
                     │  (a cut to make) │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  Execute &       │
                     │  document        │
                     └────────┬─────────┘
                              │
                    ┌─────────┴──────────┐
                    ▼                    ▼
           ┌────────────────┐   ┌──────────────────┐
           │  Dead end /    │   │  Partial truth   │
           │  failure       │   │  (keep carving)  │
           └────────┬───────┘   └────────┬─────────┘
                    │                    │
                    ▼                    ▼
           ┌────────────────┐   ┌──────────────────┐
           │  Write audit   │   │  Design next     │
           │  note if needed│   │  attempt         │
           └────────┬───────┘   └────────┬─────────┘
                    │                    │
                    └────────┬───────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Nothing left    │
                    │  but the truth   │
                    │  (project done)  │
                    └──────────────────┘
```

## Detailed steps

### 1. Define the problem

Write a `problem_statement.md` using the template. Be specific. A good problem
statement answers:

- **What is the raw marble?** What is the current state of knowledge?
- **What is the angel?** What truth do you believe is inside?
- **Why does it matter?** Who cares if this is solved?
- **What counts as done?** What does "revealed" look like?

### 2. Make an attempt

Each attempt gets a numbered file: `attempt_001.md`, `attempt_002.md`, etc.

Each attempt must contain:

- **Hypothesis** — A falsifiable claim.
- **Method** — How you'll test it (Lean proof, experiment, analysis, etc.).
- **Results** — What actually happened.
- **Failures** — Everything that went wrong. Be thorough.
- **Next steps** — What you'd try next (even if you're done with this path).

### 3. Audit when wrong

If you discover a mistake in a previous attempt, write an audit note. The
original file is **never modified** except to add a link to the audit note at
the top.

The audit note must:

- Reference the original attempt by number and date.
- State what was wrong.
- Provide the correction.
- Be dated and signed (by you or your agent).

### 4. Track citations

Use `verified_refs.md` to maintain a structured reference list. Every claim
in an attempt should trace back to a citation here.

### 5. Know your gaps

Use `gap.md` to track what you don't know. Gaps are honest, temporary, and
specific. A good gap entry says: "I assume X because Y, but Z is untested."

### 6. Reveal the truth

When all false marble has been removed — when every attempt either confirmed a
piece of the truth or was cleanly discarded — the project is done.

Write a summary. Celebrate the removed pieces as much as the revealed ones.

---

## Directory conventions

```
my-carving-project/
├── problem_statement.md   # The raw marble
├── carvings/              # Numbered attempts
│   ├── attempt_001.md
│   ├── attempt_002.md
│   ├── audit_001.md       # Audit for attempt 001
│   └── audit_002.md       # Audit for attempt 002
├── refs/
│   └── verified_refs.md   # Structured citations
├── gaps.md                # Known unknowns
└── Lean/                  # Lean 4 proofs (if applicable)
    ├── MyProof.lean
    └── AuditNotes/
```

This structure is optional but recommended. The TUI and tools will discover
any layout you use.
