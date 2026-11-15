# Eventual unique extremal inhibitory degree

Research proof draft, 2026-11-15. This note supplies the local estimates missing
from the central-window note. It is a mathematical argument, not an external
referee report. The threshold is not effective; classification at every finite
size remains open. The counting model permits redundant inputs.

## 1. Statement

Use the model and notation of [RESEARCH.md](../../RESEARCH.md). Let `D(n)` be
the number of monotone Boolean functions, and let `C(n,m)` count functions
supporting all single-high states simultaneously at a positively self-looped
node with `m` other inhibitory inputs.

**Theorem.** There is an integer `n0` such that, for every `n >= n0`,

\[
 K(n)=\{\lfloor n/2\rfloor-1\}.
\]

More precisely, for even `n=2k`,

\[
 \frac{C(2k,k-1)}{C(2k,k-2)}
 =1+(k+1)2^{-k}+O(k^{1000}2^{-2k}).                 \tag{1}
\]

For odd `n=2k+1`,

\[
 \frac{(C(n,k-2),C(n,k-1),C(n,k))}{D(n)2^{-k-3}}
 =(1,3,2)+O(k^{1000}2^{-k}),                         \tag{2}
\]

where the vector error is componentwise. The deliberately loose fixed
polynomial exponent avoids any need to optimize constants in the source's
local tail bounds. Both errors tend to zero on their relevant scales.

The theorem concerns a degree-counting observable, not attractor basins,
biological probabilities, or topology at a fixed degree sequence.

## 2. External results and their exact use

The only non-elementary input is Jenssen, Malekshahian and Park (JMP),
[*On Dedekind's problem, a sparse version of Sperner's theorem, and antichains
of a given size in the Boolean lattice*, arXiv:2411.03400v2](https://arxiv.org/html/2411.03400v2),
especially Theorem 1.7, Sections 4–5, Lemma 6.1 and Corollary 7.10.
The argument below fixes activity `lambda=1`. It does not substitute a
first-order entropy formula for a local probability estimate.

Write `L_r` for rank `r`. In a phase centered at `L_r`, a side polymer is a
2-linked set lying entirely in `L_(r-1)` or entirely in `L_(r+1)`. Its shadow
on `L_r` is `partial gamma`, and its weight is

\[
 w(\gamma)=2^{-|\partial\gamma|}.
\]

The source imposes a shadow expansion condition on the larger side layer
in odd dimension; retain that condition. Polymers are compatible exactly
when their shadows are disjoint. Sample a compatible polymer collection
with probability proportional to the product of its weights, and then
choose every unblocked central point independently with probability `1/2`.
The resulting antichain specifies the minimal true points of `f`.

For even `n`, this is the exact uniform antichain measure restricted to the
three central ranks. Its total variation distance from the full uniform
measure is `exp[-Omega(n^2)]`. For odd `n`, the equal mixture of the two
central phases has that same error. Complementing sets gives the version
centered at the lower central rank.

We also use JMP (3.6), (4.4) and the anchored cluster bound following (4.4).
With `f(gamma)=|gamma|/n^3`, the auxiliary function is

\[
g(\gamma)=\begin{cases}
 ((n-2)|\gamma|/2-|\gamma|^2)\log2-100|\gamma|\log n,
       &|\gamma|\le n/10,\\
 n|\gamma|\log2/100,&n/10<|\gamma|\le n^4,\\
 |\gamma|\log2/n^2,&|\gamma|>n^4.
\end{cases}                                                    \tag{3}
\]

For all sufficiently large `n` the source proves the Kotecky–Preiss bound
with this `f,g`, and an anchored sum at a side site is at most `n^-3`.
All singletons and all 2-linked pairs used below satisfy the source's
expansion restriction for sufficiently large `n`.

## 3. A local perturbation lemma

This is the step that cannot be obtained from an unconditional union bound
for a rare prescribed-bit event.

**Lemma 1 (localized partition ratios).** Suppose a phase is modified by
replacing each polymer weight `w(gamma)` by `h(gamma) w(gamma)`, where

* `h=1` unless the polymer meets a specified set `B` of at most `O(n^2)` side
  sites;
* `h>=0` and `h <= min(4^|gamma|, 2^(c n))` for a fixed constant `c`.

Deletion of polymers is allowed (`h=0`). If `Xi_h,Xi` are the two partition
functions, then, with `rho=2^(-n/2)`,

\[
 \log(\Xi_h/\Xi)=\sum_v (h(\{v\})-1)w(\{v\})
       +O(n^{1000}\rho^2).                              \tag{4}
\]

In particular any such ratio is `1+O(n^3 rho)`. The estimates are uniform
over the perturbations used in this note.

**Proof.** Put `a(gamma)=min(|gamma| log 4,c n log 2)` and
`g_h=g-a`. For sufficiently large `n`, (3) implies `g_h>=0` in all three
size ranges. Since

\[
 h(\gamma)w(\gamma)e^{f(\gamma)+g_h(\gamma)}
 \le w(\gamma)e^{f(\gamma)+g(\gamma)},
\]

the modified model satisfies the same KP inequality. This also holds for
any intermediate activities `w(1+s(h-1))`, `0<=s<=1`.

For a cluster of total polymer size at least a fixed integer `t`,

\[
 g_h(\Gamma)\ge t(n-2)\log2/2-O(t^2+t\log n).          \tag{5}
\]

Here is why the size ranges in (5) are uniform, including very large
polymers. If every polymer is small, each term of (3), minus
`|gamma| log 4`, is at least a positive constant times `n |gamma|`.
For total size between `t` and `n/10`, use
`sum |gamma|^2 <= (sum |gamma|)^2`; the resulting concave quadratic takes
its smaller endpoint at `t`. If the total small-polymer size exceeds
`n/10`, its contribution is `Omega(n^2)`. A medium polymer also contributes
`Omega(n^2)` after subtracting at most `c n log2`. A polymer larger than
`n^4` contributes at least `(n^2-c n)log2`. Thus none of these cases
weakens the fixed-`t` lower bound. For `t<=3`, its polynomial loss is at
most a fixed power bounded by the exponent 1000 used here.

In the difference of the two convergent log partition expansions, every
noncancelling cluster contains a polymer meeting `B`. Such a cluster is
incompatible with the singleton at at least one site in `B`. The anchored
KP bound, summed over `B`, bounds its weighted absolute sum by
`|B|/n^3`. Apply (5) with `t=2` to bound all terms except one-site
singletons by `O(n^1000 2^-n)`, in both expansions. The singleton terms
give (4). This uses the local anchored bound, not the exponentially large
global cluster sum. Exponentiating proves the last assertion. \(\square\)

**Lemma 2 (one forced side site).** Let `t` be a lower-side site, let `F`
be `O(n)` other forbidden lower-side sites, and suppose each site of `F`
is a 2-link neighbor of `t`. Write `I(t)` for all side sites whose
singleton shadows intersect the shadow of `t`, including `t` itself.
Then the phase probability that `t` belongs to the antichain and no site
in `F` does is

\[
 \begin{split}
 P(t,F)/w_t={}&1-\sum_{u\in I(t)\cup F}w_u\\
 &+\sum_{\substack{u\sim_2 t\\u\notin F}}
       \frac{w(\{t,u\})}{w_t}
 +O(n^{1000}\rho^2).
 \end{split}                                         \tag{6}
\]

The second sum runs only over distinct sites on the same side as `t`.
In all applications `w_t` is a constant multiple of `rho`.

**Proof.** Decompose according to the unique polymer containing `t`:

\[
 P(t,F)=\sum_{\substack{\gamma\ni t\\\gamma\cap F=\varnothing}}
 w(\gamma)\,\frac{\Xi_{F,\sim\gamma}}{\Xi}.             \tag{7}
\]

For the singleton root, the numerator deletes all polymers meeting `F`
or incompatible with `{t}`. Lemma 1 gives
`Xi_(F,~t)/Xi=1-sum_(I(t) union F) w_u+O(n^1000 rho^2)`.
For each two-site root use `Xi_(F,~gamma)/Xi=1+O(n^3 rho)`;
there are `O(n^2)` roots and each root weight divided by `w_t` is
`O(rho)`. Finally, the anchored original KP bound and (5) with `t=3`
bound the sum of weights of all roots of size at least three by
`O(n^1000 rho^3)`. The partition ratios in (7) are at most one.
Dividing by `w_t` gives the stated remainder. Fixed polynomial factors
from these steps can all be absorbed into the same loose exponent 1000;
the explicit losses for sizes two and three are at most 200 and 300.
\(\square\)

## 4. Even dimension: resolve the exponentially small tie

Let `n=2k`, `w=2^(-k-1)`. All side singletons have weight `w`.

### 4.1 Candidate m=k-1

Put `|Z|=k-1`. The central prescription consists of `T={Z+s} union
{Z+j:j in A}`, with one true point and `k` false points. Conditional on
the side polymers it has probability

\[
 2^{-(k+1)}\prod_{\gamma}h(\gamma).
\]

A lower polymer forcing a prescribed zero to one, or an upper polymer
forcing the prescribed one to zero, has factor zero. Otherwise its factor
is `2^|partial gamma intersect T|`.

The lower site `Z` would hit every point of `T`, but is forbidden by the
zero prescriptions. Any other lower site hits at most one point of `T`;
any upper site hits at most two. Thus the hypotheses of Lemma 1 hold with
`|B|=O(n^2)` and `c=1`, including for large polymers.

The following table counts the singleton change `(h-1)w`:

| Side site | Number | h-1 |
| --- | ---: | ---: |
| lower common site Z | 1 | -1 |
| lower subset of the true point only | k-1 | +1 |
| lower subset of a zero point only | k(k-1) | -1 |
| upper containing the true point | k | -1 |
| upper containing two zero points | binom(k,2) | +3 |

All other singleton changes are zero. Their sum is

\[
 \alpha_R w=\frac{k^2-k-4}{2}w.
\]

Consequently, writing `p_R` for the phase probability,

\[
 p_R=w\left[1+\frac{k^2-k-4}{2}w
                 +O(k^{1000}2^{-2k})\right].            \tag{8}
\]

### 4.2 Candidate m=k-2

Now `t=Z+s` has rank `k-1`, and `F={Z+j:j in A}` consists of `k+1`
forbidden sites of the same rank. Within the phase the original constraints
are exactly `t` present and `F` absent. The lower inhibitory zeros are
already implied by the activation zeros in both candidates.

The lower 2-link degree of `t` is `(k-1)(k+1)=k^2-1`. All `k+1` forbidden
sites are among these neighbors. The upper sites incompatible with `t`
are its `binom(k+1,2)` two-element extensions. A same-side pair containing
`t` has a one-point shadow overlap, so its weight is `2w^2`.
Lemma 2 gives

\[
 \begin{split}
 p_L/w
 &=1+[-1-(k^2-1)-\tbinom{k+1}{2}\\
 &\hspace{3em}+2(k^2-1-(k+1))]w+O(k^{1000}2^{-2k})\\
 &=1+\frac{k^2-5k-8}{2}w+O(k^{1000}2^{-2k}).
 \end{split}                                         \tag{9}
\]

Subtracting (9) from (8) leaves `(2k+2)w` in the relative correction.
The full-measure error, divided by either probability of order `2^-k`,
is still `exp[-Omega(k^2)]`. This proves (1), and its positive first
correction proves `C(2k,k-1)>C(2k,k-2)` for sufficiently large `k`.

## 5. Odd dimension: two unequal phase contributions

Let `n=2k+1`; call the phases centered at `L_k,L_(k+1)` lower and upper.
They have equal mixture weights up to the source's exponentially small
total variation error. With `epsilon_k=O(k^1000 2^-k)`, the leading
conditional probabilities are

| m | lower central phase | upper central phase |
| --- | --- | --- |
| k-2 | 2^(-k-2)(1+epsilon_k) | 0 |
| k-1 | 2^(-k-2)(1+epsilon_k) | 2^(-k-1)(1+epsilon_k) |
| k | O(2^(-2k)) | 2^(-k-1)(1+epsilon_k) |

For the first column in the first row, the required true site has rank
`k-1` and shadow size `k+2`; use Lemma 2 to leading order. In the upper
phase the antichain has no site below rank `k`, so this event is impossible.

For the second row the lower phase has `k+2` prescribed central bits.
The same common-site exclusion and at-most-two shadow intersection as in
Section 4 permit Lemma 1. In the upper phase a required lower side site
has shadow size `k+1`, and the other `k+1` sites are forbidden; use Lemma 2.
For the third row the upper phase has `k+1` prescribed central bits and
again admits Lemma 1.

Here are details for the small entry in the lower phase of the last row.
The `k` specified zero sites `Z+j` have rank `k+1`, where `|Z|=k`. Their
lower central shadow is

\[
 W=\{Z\}\cup\{(Z-z)+j:z\in Z,j\in A\},\quad |W|=1+k^2.
\]

Choose any `2k` members `W'` of `W`. The event requires every point of
`W'` to be false. Every lower side site meeting `W'` is forbidden, as is
each upper side site `Z+j`. Every remaining upper site meets at most two
members of `W'`: a site containing `Z` can meet only `Z`, unless it is
one of the forbidden sites; a site not containing `Z` must omit one
member of `Z` and add two outside members to meet `W` at all.
Thus the probability of these necessary conditions is
`2^(-2k) Xi_h/Xi = 2^(-2k)(1+O(k^1000 2^-k))` by Lemma 1.
This proves the upper bound in the table. Averaging the two columns gives
(2), whose largest coefficient is uniquely 3.

## 6. Localization, checked without assuming the desired ratios

For completeness the needed localization is justified here, rather than
assuming the earlier working note as an unreviewed black box.
JMP Theorem 1.7, applied separately to `f` and
`f^dagger(x)=1-f(1-x)`, shows outside probability `exp[-Omega(n^2)]` that
true points have rank at least `floor(n/2)-1`, and false points rank at
most `ceil(n/2)+1`. A required true point has rank `m+1`; if an activating
other input exists, a required false point also has rank `m+1`.
These conditions exclude all but

\[
 \lfloor n/2\rfloor-2\le m\le\lceil n/2\rceil.
\]

The endpoint with no other activators is excluded by its required false
points at rank `n-2`, for all sufficiently large `n`. A central candidate
has probability `2^-O(n)` by (8) or the second odd row, much larger than
the exceptional probability.

For the remaining right edge, in even dimension `m=k` the dual function
has `k-1` required true points of rank `k-1`, all sharing a common central
upper neighbor. In the restricted phase these must be minimal true
points and belong to one polymer of size at least `k-1`. The bound (3)
and (4.4), anchored at one required site, make this event
`exp[-Omega(k^2)]`. In odd dimension `m=k+1`, the dual has the same
`k-1` rank-`k-1` true sites. They form a linear-size lower polymer in
the phase centered at `k`, and cannot be true in the phase centered at
`k+1`. The full-measure error is still `exp[-Omega(k^2)]`.
This leaves precisely the candidates compared above, completing the proof.

## 7. Checks, limits, and priority

`python scripts/check_local_coefficients.py` enumerates the actual side
sites and shadows, independently of the closed polynomial simplifications.
It checks the modified singleton sum, the rooted pair/deletion sum, the
two-site shadow intersection and the odd zero-shadow geometry. This is
a finite audit of the algebra, not a substitute for Lemmas 1–2.

The 2026 GRN source poses the general inhibitory-degree maximization
question in Section 6.3. The present draft uses established antichain
machinery; it does not claim to invent that machinery. Searches on
2026-11-15 for the paper title, DOI, extremal inhibitory counts and the
repository found the source article/preprint and no separate solution.
That bounded search is not an exhaustive priority guarantee.

Still required before a submission claim: external expert proof review,
particularly of the localized KP perturbation in Lemma 1; a further
forward-citation check; an authored manuscript and agreed author metadata.
No external reviewer or independent agent has reviewed this draft.
An effective threshold and an all-`n>=5` classification are not proved.
