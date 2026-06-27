# Attempt 002: Direction field oscillation as a blow-up criterion

> **Date:** 2025-11-11
> **Author:** marble-carver demo
> **Status:** Completed

---

## Hypothesis

Blow-up occurs when the vorticity direction field ξ(x,t) = ω/|ω| has
persistent, large-amplitude oscillations at small scales. More precisely, if
the L¹ norm of the gradient of ξ fails to be integrable in time, then the
solution becomes singular.

This is the contrapositive of the Constantin-Fefferman regularity criterion,
which says that if the solution is smooth on [0,T), then

∫₀ᵀ ‖∇ξ(·,t)‖_{L^∞} dt < C.

## Method

1. Formalize the Constantin-Fefferman theorem statement.
2. Attempt to construct a counterexample — a scenario where ‖∇ξ‖_{L^∞} is not
   integrable in time, and check whether the implied rough direction field can
   be consistent with the NS equations.
3. Begin Lean formalization of the geometric regularity criterion (see
   `math/`).

**Key references:** [Constantin-Fefferman 1993], [Constantin 2007]

## Results

### What worked

- The contrapositive holds by standard logic.
- A toy model (1D complex Burgers) exhibits exactly this behavior: direction
  field oscillation precedes blow-up.

### What didn't work

- The 3D NS case is radically different from 1D Burgers — the pressure Hessian
  couples direction field evolution to the velocity field in a nonlocal way.
- No clean counterexample could be constructed in 3D.

## Failures

| # | What failed | Why | What it ruled out |
|---|-------------|-----|-------------------|
| 1 | 1D analogy | NS pressure is nonlocal; Burgers lacks pressure | 1D intuitions don't transfer directly |
| 2 | Explicit counterexample | Could not satisfy incompressibility + oscillation | The coupling may prevent pathological oscillation |

## Next steps

- [ ] Attempt Lean formalization of the CF criterion.
- [ ] Search for numerical experiments on direction field oscillation in
      near-blow-up flows.

## Key references

- Constantin-Fefferman (1993). Direction of vorticity and the problem of
  global regularity for the Navier-Stokes equations. *Indiana Univ. Math. J.*
- Constantin (2007). Geometric statistics in turbulence.
