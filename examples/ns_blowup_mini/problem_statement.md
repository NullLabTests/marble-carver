# Problem statement: Navier-Stokes blow-up criteria (mini)

> **Date:** 2025-11-01
> **Author:** marble-carver demo
> **Domain:** Mathematics / PDEs

---

## The marble

The Navier-Stokes equations govern fluid flow. Despite their importance, it
remains unknown whether smooth solutions can develop singularities (blow up)
in finite time in 3D. This is one of the Clay Millennium Problems.

Current knowledge: existence of weak solutions (Leray), partial regularity
(Caffarelli-Kohn-Nirenberg), and conditional regularity criteria (Prodi,
Serrin, Ladyzhenskaya).

## The angel

A specific, checkable criterion that guarantees smooth solutions exist for all
time — or a concrete blow-up mechanism. The truth is already in the equations;
we just need to carve away the wrong approaches.

## Why this matters

Beyond the Clay prize: turbulence modelling, weather prediction, and
aerodynamic design all depend on understanding NS regularity.

## Definition of done

A conditional regularity result in Lean 4, or a documented blow-up scenario
with rigorous justification.

## Initial gaps

- [ ] How do vorticity stretching terms behave near a potential singularity?
- [ ] Can the Caffarelli-Kohn-Nirenberg theorem be formalized in Lean?
