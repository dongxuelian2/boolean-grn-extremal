# Anonymous manuscript package

Title: **The eventual extremal inhibitory degree for simultaneous single-high multistability**.

The full paper is `manuscript/main.tex`, including abstract, model, theorem,
proofs, explicit conditional finite certificate, interpretation and bibliography.
The author block is intentionally empty at the user's request. This package
does not state that a journal submission or human peer review has occurred.

Build with:

```sh
bash scripts/build_manuscript.sh
```

This requires a standard LaTeX installation with pdfLaTeX, AMS packages,
Latin Modern, microtype and hyperref. No bibliography service, network
connection or external figure is needed to compile. Output is
`output/manuscript/grn-extremal-manuscript.pdf`.

Reproduce the computational audits with:

```sh
python scripts/check_local_coefficients.py
python scripts/check_grn_local_threshold.py
python -m unittest discover -s tests -v
```

The second script proves no external source inequality at a chosen numeric
dimension: it checks the elementary logarithmic inequalities accompanying
the conditional certificate. The paper does **not** assert a numerical
unconditional cutoff. Source-global constant extraction and an all-size
classification remain distinct research questions.

The independent internal review and integrated-paper review are recorded
in `docs/research/independent-grn-review-2026-11-15.md`. The reviewer was
a separately instructed model agent, not an external human referee.

The manuscript is journal-neutral. The Electronic Journal of Combinatorics
is a scope-compatible option; its [current author instructions](https://www.combinatorics.org/ojs/index.php/eljc/about/submissions)
accept a PDF and abstract at initial submission and require author metadata.
No venue or author identity has been selected on the user's behalf.
