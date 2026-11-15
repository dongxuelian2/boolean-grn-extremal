# Eventual-extremum proof audit, 2026-11-15

## Manuscript continuation

The full paper `manuscript/main.tex` is now complete and incorporates an
independent model-agent review and integration review. It proves the explicit
local envelope and conditional certificate; these do not establish an
unconditional numerical threshold. All 6 final PDF pages were rendered and
inspected; the final LaTeX log has no missing-reference or overflow warning.
The local-coefficient script, conditional-threshold script and all 3 reference
tests passed. An anonymous source/PDF package and covering-letter text are
provided; author identity is omitted at the user's request. The original
pre-review snapshot below is retained as history.

## Initial proof-note snapshot

Scope: the new [proof draft](eventual_extremal_classification.md), not an
all-size classification or an external referee report.

* Re-read JMP arXiv:2411.03400v2 Theorem 2.2, Theorem 1.7, polymer
  definitions in Sections 4–5, (3.6), (4.4), Lemma 6.1, Section 7.2 and
  Corollary 7.10. Retained the odd-phase shadow-expansion restriction.
* Derived the local perturbed KP bound with a **capped** activity gain:
  `min(4^|gamma|,2^(c n))`. Using only `4^|gamma|` would not justify the
  large-polymer tail; using only an unconditional blocker probability
  would not control the rare prescribed-bit event.
* Re-derived both even coefficients by counting side shadows, including
  the root's own exclusion and two-site root polymers. Their difference
  is `2k+2` in units of `2^(-k-1)`.
* Rechecked odd phases separately and bounded the suppressed contribution
  using `2k` necessary central zeros, rather than assuming phase symmetry
  for the constrained event.
* `python scripts/check_local_coefficients.py`: passed at `k=2,...,7`.
  This verifies finite geometry/algebra, not the unbounded analytic tail.
* `python -m unittest discover -s tests -v`: all 3 reference tests passed.
* `git diff --check`: passed.
* `bash scripts/build_proof_pdf.sh`: PDF compiled; all 6 pages rendered
  and visually inspected, with no clipped equations or missing symbols.

No external reviewer or second agent was used. No effective `n0`, new
large-`n` enumeration, journal acceptance, or exhaustive novelty clearance
is asserted. Original DOI/title searches found the source article and
preprint, and no separate solution within that bounded search.
