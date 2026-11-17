# Independent review of the eventual-extremum proof

Date: 2026-11-15. Reviewer: a separately instructed model subagent, not a
human referee or an external subject expert. Reviewed the existing proof
without editing it, re-read the primary antichain inputs, and re-derived
the local coefficient and tail arguments. This report is not a claim of
formal proof verification or journal acceptance.

## Finding

I found no counterexample or fatal logical error in the eventual
classification argument. The positive even correction and odd `1:3:2`
weights survive the checks below. The main presentational deficiency is
that the `O(n^1000 2^-n)` tail is left without an explicit envelope. It can
be replaced by a conditional numerical local bound. A numerical local
bound must not be advertised as an unconditional cutoff for the complete
Boolean lattice.

The word **ineffective** should be replaced by **not explicit / not
numerically extracted**. There is no demonstrated intrinsic
ineffectivity in the constructive combinatorial inputs.

## Published-version cross-check

In addition to arXiv:2411.03400v2, I checked the
[published JMP version, JLMS 114 (2026), e70624](https://londmathsoc.onlinelibrary.wiley.com/doi/epdf/10.1112/jlms.70624).
The references needed here retain their numbering and mathematical
content:

| Input | Published pages |
| --- | --- |
| Theorem 1.7, full-to-central antichain approximation | 7 |
| Theorem 2.2, KP convergence and anchored cluster bound | 9 |
| Formula (3.6), auxiliary function g | 15 |
| Formula (3.13), anchored estimate | 17 |
| Section 4 definitions and formula (4.4) | 18-20 |
| Section 5 sampling description | 23 onward |
| Lemma 6.1, exact even restricted measure | 33 |
| Corollary 7.10, odd equal-phase approximation | 44-45 |

The central-phase weights are the simplified three-layer weights, not
the four-layer weights with an interior sum. The odd expansion condition
on the larger side layer remains necessary and was retained by the
reviewed proof. I found no relevant change between the cited preprint
formulas and the published formulas.

## Local perturbation audit

The modified KP argument is sound because, with
`a(gamma)=min(2|gamma|,n) log 2` and `g_h=g-a`, each modified weighted
KP summand is bounded by its original counterpart. Zero activities are
allowed. Clusters unaffected by the perturbation cancel before applying
an absolute tail bound. An affected cluster contains a polymer meeting
the touched-site set and is therefore incompatible with the singleton at
one of those sites. This justifies an anchored bound proportional to the
number of touched sites. Applying the exponentially large global
cluster bound at this point would not establish the claimed error.

The cap at `2^n` is essential for the present proof: `g` has slope only
`log 2/n^2` for very large polymers, so subtracting `2|gamma| log 2`
without that cap would fail.

### Explicit envelope under the source KP inequality

The following is a deliberately conservative quantitative replacement.
Let

\[
 N_*=2^{20}=1048576,\qquad \rho=2^{-n/2}.
\]

Assume the original source KP inequality with `f(gamma)=|gamma|/n^3`
and its function `g` holds at dimension `n`. The condition is an explicit
assumption here; the source proves that it eventually holds but does not
supply a ready-to-use numerical starting dimension.

For `n>=N_*` and `t=2,3`, every cluster with norm at least `t` obeys

\[
 g_h(\Gamma)\ge L_t(n)
 =\left(\frac{n-6}{2}t-t^2\right)\log 2-100t\log n.       \tag{R1}
\]

Here are explicit uniform reasons, including the large-size regimes.
For a small polymer of size `s<=n/10`,

\[
 g_h(\gamma)\ge H_n(s)
 =\left(\frac{n-6}{2}s-s^2\right)\log2-100s\log n
 \ge ns\log2/4.                                         \tag{R2}
\]

For the final inequality, use `log2 n<=sqrt(n)` for `n>=16`; at
`n>=2^20`, `(2n/5-3)-100 log2 n >= n/4`. If the total small-polymer
norm is between `t` and `n/10`, the inequality
`sum s_i^2 <= (sum s_i)^2` reduces the issue to the concave quadratic
`H_n(S)`, whose minimum on that interval occurs at an endpoint. The
upper endpoint is at least `n^2 log2/40`, and this exceeds `L_3(n)`.
If the total small-polymer norm exceeds `n/10`, (R2) gives the same
quadratic bound. A medium polymer contributes at least
`(n^2/1000-n)log2`, and a polymer of size greater than `n^4`
contributes at least `(n^2-n)log2`. Both exceed `L_3(n)` for the
stated `N_*`. Other summands are nonnegative. This proves (R1).

In particular,

\[
 e^{-L_2}=2^{10}n^{200}\rho^2,\qquad
 e^{-L_3}=2^{18}n^{300}\rho^3.                            \tag{R3}
\]

In every application in the note a touched-site bound `|B|<=4n^2`
suffices. For a central prescription, the side sites touching its
`O(n)` prescribed points number at most `n|T|`; the extra explicitly
forbidden sites in the suppressed odd event number at most `n`.
For one or two rooted sites, their incompatible singleton sites number
at most `n^2` per root plus at most `n` forbidden sites. Thus `4n^2`
is a common conservative envelope.

The difference between the two logarithmic partition functions has
tail at most

\[
 \frac{2|B|}{n^3}e^{-L_2}
 \le 2^{13}n^{199}\rho^2.                               \tag{R4}
\]

The singleton part has absolute value at most `12n^2 rho`, since each
singleton multiplier lies in `[0,4]` and each singleton weight is at
most `rho`. For `n>=N_*` these quantities are much less than one.
Taylor's elementary bound `|exp(x)-1-x|<=x^2` for `|x|<=1/2`,
with a separate bound for the logarithmic tail, gives an error at most
`2^15 n^200 rho^2` after exponentiation.

For the rooted formula, the singleton-deletion contribution has that
same envelope. Each allowed two-site root has weight divided by the
root weight at most `2rho`, at most `n^2` such roots occur, and its
deletion ratio differs from one by at most `8n^2 rho`. The extra error
is therefore at most `16n^4 rho^2`. The sum of roots of size at least
three, after division by the root weight, is at most

\[
 \frac{4}{\rho}\,n^{-3}e^{-L_3}
 =2^{20}n^{297}\rho^2.                                  \tag{R5}
\]

The factor `4/rho` safely covers the smallest singleton weight in both
odd and even phases. All these errors are bounded by

\[
 R(n)=2^{24}n^{300}\rho^2.                               \tag{R6}
\]

Consequently both even normalized candidate expansions in the draft
hold with an explicit error bounded by `R(n)` at `n>=N_*`, conditional
on the source KP inequality. No unspecified big-O constant remains in
this local assertion.

## Independent coefficient and phase checks

I re-derived the even rooted coefficient by summing over **all** possible
second side-defect sites, subtracting the full denominator's singleton
coefficient, rather than counting only the local rooted neighbors.
For `k=2,3,4,5`, this gives

| k | central coefficient | rooted coefficient |
| ---: | ---: | ---: |
| 2 | -1 | -7 |
| 3 | 1 | -7 |
| 4 | 4 | -6 |
| 5 | 8 | -4 |

These match `(k^2-k-4)/2` and `(k^2-5k-8)/2` respectively. In the
general calculation the difference is `2k+2`; the root's self-exclusion
and the removal of the forbidden root neighbors are both needed.
This is a finite algebra audit, not a proof of the analytic tail.

For odd dimensions the three rows correspond to genuinely different
constraints in the two phases. The impossible upper-phase first row is
indeed impossible: the required true point lies below every possible
minimal true point of that phase. The last-row lower-phase suppression
uses a necessary zero event on `2k` central points. A permitted upper
side site meets at most two of them; lower sites meeting them are
forbidden. The activity perturbation therefore satisfies the same cap
and locality hypotheses. No equal-phase symmetry is incorrectly imposed
on the constrained probabilities.

## A finite global certificate, and its limitation

The local gap between the even phase probabilities is

\[
 p_R-p_L\ge \frac{n+2}{8}\rho^2 \quad(n\ge N_*).          \tag{R7}
\]

Indeed, its leading value is `(n+2)rho^2/4` and its remainder is at
most `rho R(n)`. The inequality needed to make this remainder at most
half the leading term is

\[
 27+300\log_2 n-\frac n2-\log_2(n+2)\le0.                \tag{R8}
\]

It holds for every `n>=2^20`, for example by bounding `log2 n` by
`sqrt(n)` and checking the resulting decreasing upper envelope.

Here is a sufficient **finite-dimensional global certificate**:

1. `n>=2^20`;
2. the source central-phase KP inequality holds at dimension `n`;
3. the full uniform antichain measure is within TV distance `2^(-2n)`
   of the even three-rank phase or the odd equal two-phase mixture.

Under these conditions the draft's complete extremal classification
holds at that dimension. For even `n`, (R7) exceeds twice the global
TV error. For odd `n`, each nonzero entry of the conditional phase table
has relative error at most `16n^2 rho`; (R6) is already smaller than
`n^2 rho`, and the suppressed entry contributes at most `2^(1-2k)`.
After dividing the mixture probabilities by `2^(-k-3)`, each coordinate
of the error from `(1,3,2)` is at most `64n^2 rho`.
The inequality `256n^2 rho<=1` holds at and above the stated `N_*`.
The resulting gap exceeds half the leading unit
`2^(-k-3)` at this `N_*`, which also exceeds twice the TV error.

The localization follows from the same TV condition, applied also to
the uniformly distributed dual function. Outside the candidate window
the necessary true/false rank event has phase probability zero. The
remaining right edge requires one lower-side polymer of size at least
`floor(n/2)-1`. Its probability is at most
`n^-3 2^(-n^2/300)` using the source anchored weight bound and (3.6),
plus the TV error. This is smaller than a central candidate probability.

The third certificate condition follows eventually from JMP, but it is
not established numerically at `n=2^20` merely by this calculation.
Likewise the source KP inequality is not established at that numerical
dimension by invoking an unspecified asymptotic constant. Thus
`2^20` is a **conditional local threshold**, not a numerical global
cutoff. Source-global constant extraction additionally has to cover
the embedding dimensions between `n` and `2n` in Section 3 and the
odd-phase multiplicity estimates. A finite all-size verification below
an actually proved cutoff would still be needed for an all-`n`
classification.

## Verification script and remaining editorial corrections

`python scripts/check_grn_local_threshold.py` evaluates the logarithmic
inequalities and the independent global two-defect coefficient
extraction without constructing astronomically large powers. The
extension to every `n>=2^20` is proved by the monotone bounds above;
sampling a few larger dimensions is only an implementation check.

For a submission manuscript:

* State and cite the published JMP version, and make the phase sampling
  convention and the odd expansion restriction explicit.
* Replace the informal auxiliary `O` bounds with the local envelope
  (R6), or an equally explicit proved bound.
* Separate the eventual theorem, conditional finite certificate, and
  unsolved extraction of an unconditional numerical cutoff.
* Describe this independent model-agent review accurately; do not call
  it external peer review or a human expert review.

The independent audit supports proceeding to an eventual-classification
manuscript after these edits. It does not establish the all-size theorem
or grant priority/novelty clearance.

## Integration review of manuscript/main.tex

I subsequently reviewed the integrated LaTeX manuscript, including its
explicit local lemmas and finite-certificate theorem. No fatal mismatch
with this report was found. The following explanatory additions were
recommended to the parent author:

1. Record the bridge `R(n)<=n^2 rho` at `n>=2^20`. It follows from
   `24+298 log2 n<=n/2`; use `log2 n<=sqrt(n)` and the decreasing
   upper envelope `24+298sqrt(n)-n/2`. Each central/root leading phase
   entry then has relative error at most `16n^2 rho`. Thus the displayed
   odd `O(n^3 rho)` is valid (indeed weaker), and the finite odd vector
   error bound `64n^2 rho` has an explicit route from the lemmas.
2. Give the touched-site count when applying the perturbation lemma:
   `n|T|+n<=2n^2` for the central prescriptions and suppressed event,
   and at most `3n^2` for the rooted deletion gases. These imply the
   common `4n^2` envelope without an asymptotic cardinality convention.
3. When deriving the even ratio, state `p_L/w=1+O(n^2 rho)` explicitly.
   Dividing by it changes the retained correction only by a polynomial
   times `rho^2`, which is within the claimed remainder.

The published GRN title, article number and first author's surname and
initials agree with the
[Springer record](https://link.springer.com/article/10.1007/s11538-026-01791-4)
and Crossref DOI metadata: B. V. Harshavardhan, Sarah Adigwe, Mohit Kumar
Jolly, and Tomáš Gedeon. The manuscript's abbreviated author names are
valid. The bibliographic form is not evidence about the theorem's
novelty, which requires its separate priority audit.
