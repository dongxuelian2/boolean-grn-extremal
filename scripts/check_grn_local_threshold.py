#!/usr/bin/env python3
"""Conditional local-threshold and separate coefficient audit.

Does not verify the external KP inequality or full-lattice TV bound at any
numerical dimension. See independent-grn-review-2026-11-15.md for proofs
extending the elementary inequalities to all n>=2**20.
"""
from fractions import Fraction
from itertools import combinations
from math import log2


LOCAL_N = 2**20


def log_margins(n):
    assert n >= LOCAL_N
    return {
        "small_g_minus_n_s_over_4": (3*n/20-3)-100*log2(n),
        "phase_gap_log_margin": n/2+log2(n+2)-27-300*log2(n),
        "remainder_below_n2rho_log_margin": n/2-24-298*log2(n),
        "singleton_log_abs_below_quarter_margin": n/2-6-2*log2(n),
        "medium_tail_over_L3": n*n/1000-n-(3*n/2-18-300*log2(n)),
    }


def layer(n, rank):
    return [frozenset(x) for x in combinations(range(n), rank)]


def direct_coefficients(k):
    """Use all second-defect sites and the full denominator coefficient."""
    n = 2*k
    center = layer(n, k)
    sides = layer(n, k-1)+layer(n, k+1)
    shadows = {v: {x for x in center if v < x or x < v} for v in sides}
    z = frozenset(range(k-1))
    true = z | {k-1}
    zeros = {z | {j} for j in range(k, n)}
    central = 0
    for v in sides:
        hits = shadows[v] & (zeros | {true})
        conflict = bool(hits & zeros) if len(v) < k else true in hits
        central += (0 if conflict else 2**len(hits))-1

    z = frozenset(range(k-2))
    root = z | {k-2}
    forbidden = {z | {j} for j in range(k-1, n)}
    numerator_degree_two = 0
    for v in sides:
        if v == root or v in forbidden or v < root or root < v:
            continue
        numerator_degree_two += 2**len(shadows[root] & shadows[v])
    rooted = numerator_degree_two-len(sides)
    assert central == Fraction(k*k-k-4, 2)
    assert rooted == Fraction(k*k-5*k-8, 2)
    return central, rooted


def main():
    for n in [LOCAL_N, LOCAL_N+1, 2*LOCAL_N, 4*LOCAL_N]:
        margins = log_margins(n)
        assert min(margins.values()) > 0
        print(f"n={n}: {margins}")
    for k in range(2, 6):
        print(f"k={k}: central/rooted coefficients={direct_coefficients(k)}")
    print("PASS: elementary local envelopes and finite coefficient algebra")
    print("NOT VERIFIED: external KP and global TV inequalities at n=2**20")


if __name__ == "__main__":
    main()
