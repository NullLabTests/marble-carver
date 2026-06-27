# Attempt 002: Structural mimicry via Alphafold analysis

> **Date:** 2025-12-10
> **Author:** marble-carver demo
> **Status:** Completed

---

## Hypothesis

Structural similarity between CVB proteins and β-cell autoantigens (GAD65,
IA-2, insulin) extends beyond linear sequence motifs. If a CVB protein
presents a surface patch structurally homologous to a β-cell epitope, T-cell
cross-reactivity may occur even without sequence identity.

## Method

1. Download Alphafold models for CVB proteins (P2-C, VP1, 3C) and β-cell
   autoantigens (GAD65, IA-2, preproinsulin).
2. Compute structural alignments (TM-align) for all pairs.
3. Identify surface-exposed regions with TM-score > 0.5.

**Tools:** Alphafold DB, TM-align, PyMOL visualization.

## Results

### What worked

- P2-C has a surface loop (residues 32-48) with structural homology to a known
  T-cell epitope on GAD65 (TM-score 0.58).
- This homology is not detectable by sequence alignment alone (sequence
  identity < 20% in the aligned region).
- The homologous surfaces are enriched in HLA-DR4 binding motifs.

### What didn't work

- No significant structural homology found between VP1/3C and IA-2/insulin.
- The confidence of the P2-C loop prediction is lower (pLDDT ~72) than the
  rest of the protein.

## Failures

| # | What failed | Why | What it ruled out |
|---|-------------|-----|-------------------|
| 1 | VP1/3C mimicry | No structural homology | Only P2-C has detectable mimicry in current data |
| 2 | High-confidence prediction for the loop | pLDDT 72 is moderate | Need experimental validation |

## Next steps

- [ ] Check AlphaFold3 or experimental structures for the P2-C loop.
- [ ] Design peptide-MHC tetramers to test T-cell cross-reactivity
      experimentally.
- [ ] Formalize the T1DM mechanism as a structured `mechanism` project.
