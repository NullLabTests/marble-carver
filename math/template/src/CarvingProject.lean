/-
# CarvingProject

A Lean 4 carving project using mathlib.

This template demonstrates the marble-carver workflow within Lean:
- Statement of a theorem or problem.
- Numbered lemmas representing carving attempts.
- `sorry` placeholders for unproven claims.
- Audit notes for corrected claims.

The goal is not to prove everything at once, but to carve toward the truth
one `sorry` at a time.
-/

import Mathlib

open Real

/-! ## Problem statement

The marble: Every continuous function on a compact set is uniformly
continuous (Heine-Cantor theorem).

The angel: A clean, constructive proof using the open cover definition of
compactness.
-/

/-! ### Attempt 1: Sequential compactness approach

Uses the fact that compact ⟹ sequentially compact in metric spaces.
-/
theorem heine_cantor_sequential {X Y : Type _} [MetricSpace X] [MetricSpace Y]
    (f : X → Y) (hX : CompactSpace X) (hf : Continuous f) : UniformContinuous f :=
by
  -- This approach requires sequential compactness, which holds in metric spaces.
  -- The proof is straightforward but needs careful epsilon-delta bookkeeping.
  sorry


/-! ### Attempt 2: Open cover approach

Uses the open cover definition directly with Lebesgue numbers.

[Audit note needed?] See audit_001.md for a discussion of a subtle issue
with the Lebesgue number lemma in non-metric spaces.
-/
theorem heine_cantor_open_cover {X Y : Type _} [MetricSpace X] [MetricSpace Y]
    (f : X → Y) (hX : CompactSpace X) (hf : Continuous f) : UniformContinuous f :=
by
  -- Use the Lebesgue number lemma.
  -- Given ε > 0, for each x, there exists δ_x > 0 such that ...
  -- The open cover { B(x, δ_x/2) } has a Lebesgue number δ > 0.
  -- Then for any d(x, x') < δ, we have d(f(x), f(x')) < ε.
  sorry


/-! ### Attempt 3: Direct epsilon-delta with finite subcover

A more explicit constructive approach.
-/
theorem heine_cantor_constructive {X Y : Type _} [MetricSpace X] [MetricSpace Y]
    (f : X → Y) (hX : CompactSpace X) (hf : Continuous f) : UniformContinuous f :=
by
  intro ε hε
  have hpos : 0 < ε / 2 := by linarith
  -- For each x, continuity gives δ_x.
  -- Take the finite subcover, then min δ_x/2
  sorry


/-! ## Gaps

Each `sorry` above is a gap in the carving. As gaps are resolved, the
`sorry` is replaced with a proof and the gap is closed in `gaps.md`.

## Tracking progress

- Number of sorries: 3
- Completed proofs: 0
- Audit notes: 0
-/
