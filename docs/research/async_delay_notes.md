# Separate research track: optimal delay placements in an asynchronous star example

**Model-warning:** This is **not** the complete signed-monotone positive-self-loop model used for \(C(n,m)\). Do not combine the counts or the biological interpretations without an explicit reduction.

Source: Pastva et al., 2025, motif-avoidant attractors in asynchronous Boolean networks, [DOI 10.1007/s00285-025-02235-8](https://doi.org/10.1007/s00285-025-02235-8), Supplement A.2, Claims 1–5. Their sharp star-example bound of \(\lfloor N^2/4\rfloor\) delay edges is **prior work**, not rediscovered here.

## A necessary profile for a minimum-size solution

Let \(d_i\) count delayed incoming edges at vertex \(i\). Following the sequence of first activations on a reachable path to the all-ON target and counting unresolved predecessor inputs yields the necessary inequalities

\[
\#\{i:d_i\ge r\}\ge N-2r+1,\qquad
1\le r\le\lfloor N/2\rfloor.
\]

Summing over \(r\) recovers the known minimum-edge bound. If the bound is attained, every layer inequality must attain equality. Therefore the degree **multiset** is necessarily

\[
N=2q:\quad \{0,1,1,2,2,\ldots,q-1,q-1,q\},
\]
\[
N=2q+1:\quad \{0,1,1,2,2,\ldots,q,q\}.
\]

This is a derived necessary condition; it does **not** characterize which individual edges may be delayed, and it does not upgrade the cited source's extremal edge count to a new theorem.

## Why degree data are insufficient

For \(N=3\), delaying only self-edges \(2\to2\) and \(3\to3\) has minimum cardinality and degree multiset \(\{0,1,1\}\), yet the prescribed all-ON original-variable state cannot be reached along the required asynchronous dynamics. When exactly one original variable is ON, no other vertex sees its non-self inputs all 0 or all 1, so an additional \(0\to1\) transition is unavailable. The precise update convention is the one of Pastva et al.; check it before trying generalizations.

**Next theorem target:** classify edge placements that are sufficient given the necessary profile, or derive an independently checkable reachability criterion. A degree-only classification is already falsified by the three-node example. Work with complete reachability proofs rather than more delay-count tables.