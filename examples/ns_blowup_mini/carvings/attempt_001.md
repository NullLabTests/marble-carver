# Attempt 001: Vorticity alignment as a blow-up criterion

> **Date:** 2025-11-01
> **Author:** marble-carver demo
> **Status:** Superseded (see [audit_001.md](audit_001.md))

---

## Hypothesis

If the vorticity direction field becomes pathologically aligned with the
eigenvectors of the strain tensor, then enstrophy growth becomes unbounded,
implying finite-time blow-up.

## Method

Literature review and formal calculation:

1. Derive the evolution equation for enstrophy ∫|ω|² dx.
2. Express the vortex stretching term as ω·S·ω where S is the rate-of-strain
   tensor.
3. Identify geometric conditions that prevent cancellation.

**Key references:** [Constantin-Fefferman 1993], [Gibbon 2008]

## Results

### What worked

- The enstrophy production term can be expressed entirely as a function of the
  alignment between vorticity and strain eigenframes.
- In 2D, this term vanishes exactly — consistent with global regularity.

### What didn't work

- The alignment condition that maximizes growth (vorticity parallel to the
  most contracting eigendirection) also creates strong dissipation. The net
  balance is unclear without further assumptions.
- The known 3D singularity scenarios (e.g. Kida-Pelz initial data) suggest
  alignment dynamics are more complex than the simple model.

## Failures

| # | What failed | Why | What it ruled out |
|---|-------------|-----|-------------------|
| 1 | Simple alignment model | Neglects pressure Hessian coupling | Pure alignment without pressure is insufficient |
| 2 | Assumed constant alignment | Alignment angle evolves dynamically | Need dynamic model |

## Next steps

- [ ] Formulate a model that includes pressure Hessian effects.
- [ ] Check the Constantin-Fefferman geometric regularity criterion for
      possible formalization.

---

*This attempt is superseded — see [audit_001.md](audit_001.md) for the
correction.*
