# Audit Note 001

> **Date:** 2025-11-10
> **Author:** marble-carver demo
> **Original attempt:** [attempt_001.md](attempt_001.md)

---

## Scope

Addresses the hypothesis and conclusions in attempt 001.

## Original claim (unchanged)

> "If the vorticity direction field becomes pathologically aligned with the
> eigenvectors of the strain tensor, then enstrophy growth becomes unbounded,
> implying finite-time blow-up."

This text remains at `attempt_001.md` and is not modified.

## What was wrong

The claim overlooks the **depletion phenomenon** identified by
Constantin-Fefferman: when vorticity aligns with the strain eigenframe, the
nonlinear term can actually *deplete* rather than amplify. The claim assumed
alignment → growth, but alignment is known to correlate with regularity in
certain regimes.

## Correction

Alignment between vorticity and strain eigenvectors is not sufficient for
blow-up. In fact, the Constantin-Fefferman geometric regularity criterion
shows that *some* alignment is actually present in regular solutions. The
criterion that separates blow-up from regularity is more subtle: it involves
the *oscillation* of the vorticity direction, not just its alignment.

## Impact

- Attempt 001's hypothesis is not valid as stated.
- The geometric approach itself is sound; the framing was wrong.
- Next attempts should focus on direction field oscillation, not simple
  alignment.

## Lessons

Always check whether the proposed mechanism is already known to be compatible
with regularity. The depletion phenomenon should have been caught earlier.
