# Attempt 001: P2-C peptide similarity hypothesis

> **Date:** 2025-12-01
> **Author:** marble-carver demo
> **Status:** In Progress

---

## Hypothesis

The coxsackievirus B (CVB) P2-C protein contains a peptide motif
(PEVKEK) that is structurally similar to the β-cell autoantigen GAD65
(amino acids 247–279). This mimicry triggers cross-reactive T cells in
individuals with HLA-DR4, leading to β-cell destruction.

## Method

1. Sequence alignment: P2-C vs. GAD65 using BLAST and structure prediction.
2. Literature search for T-cell cross-reactivity data.
3. Compile reported cases.

**Key references:** [Kaufman 1992] (PMID: 1379422), [Atkinson 1994]
(PMID: 7513430)

## Results

### What worked

- The PEVKEK motif in P2-C shares 5/6 amino acids with the GAD65 sequence
  (PEVKEK vs. PEVKEK — actually exact match in a 6-mer window).
- HLA-DR4 binding predictions are positive for both peptides.
- Multiple studies report CVB-specific T cells that also respond to GAD65.

### What didn't work

- The exact epitope recognized by cross-reactive T cells varies between
  studies.
- Protection vs. promotion: some studies find CVB infection *protects* against
  T1DM in NOD mice.
- Temporal sequence is unclear: infection may occur years before diagnosis.

## Failures

| # | What failed | Why | What it ruled out |
|---|-------------|-----|-------------------|
| 1 | Simple "infection → autoimmunity" chronology | Onset is heterogeneous | Naive linear causality |
| 2 | Single epitope model | Multiple epitopes reported | The mimicry may be polyclonal |

## Next steps

- [ ] Audit literature for the conflicting "protective" CVB results.
- [ ] Search for structural similarity (not just sequence) using Alphafold.
- [ ] Expand to other enteroviral proteins (VP1, 2C, 3C).

## Key references

- Kaufman et al. (1992). PMID: 1379422
- Atkinson et al. (1994). PMID: 7513430
