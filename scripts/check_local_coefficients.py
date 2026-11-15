#!/usr/bin/env python3
"""Finite algebra/geometry audit for the eventual-extremum proof.

Enumerates subsets and their actual shadows; does not enumerate monotone
functions or verify the analytic cluster-expansion remainder.
"""
from fractions import Fraction
from itertools import combinations


def layer(n, r):
    return [frozenset(s) for s in combinations(range(n), r)]


def shadow(v, n, r):
    if len(v) == r - 1:
        return frozenset(v | {i} for i in range(n) if i not in v)
    if len(v) == r + 1:
        return frozenset(v - {i} for i in v)
    raise ValueError("not a side site")


def even_coefficients(k):
    n, r = 2*k, k
    z = frozenset(range(k-1))
    s = k-1
    true = z | {s}
    zeros = {z | {j} for j in range(k, n)}
    prescribed = zeros | {true}
    central_coefficient = 0
    for rank in [r-1, r+1]:
        for v in layer(n, rank):
            hits = shadow(v, n, r) & prescribed
            conflict = bool(hits & zeros) if rank < r else true in hits
            multiplier = 0 if conflict else 2**len(hits)
            central_coefficient += multiplier-1

    z = frozenset(range(k-2))
    s = k-2
    root = z | {s}
    forbidden = {z | {j} for j in range(k-1, n)}
    root_shadow = shadow(root, n, r)
    deleted = 0
    rooted_pair_weight = Fraction(0)
    for rank in [r-1, r+1]:
        for v in layer(n, rank):
            v_shadow = shadow(v, n, r)
            if v_shadow & root_shadow or v in forbidden:
                deleted += 1
            if rank == r-1 and v != root and v_shadow & root_shadow and v not in forbidden:
                assert len(v_shadow & root_shadow) == 1
                # w({root,v}) / (w_root * w_v).
                rooted_pair_weight += 2**len(v_shadow & root_shadow)
    rooted_coefficient = rooted_pair_weight-deleted
    want_central = Fraction(k*k-k-4, 2)
    want_rooted = Fraction(k*k-5*k-8, 2)
    assert (central_coefficient, rooted_coefficient) == (want_central, want_rooted)
    assert central_coefficient-rooted_coefficient == 2*k+2
    return central_coefficient, rooted_coefficient


def odd_geometry(k):
    n, r = 2*k+1, k
    z = frozenset(range(k))
    zeros = {z | {j} for j in range(k+1, n)}
    central_shadow = set().union(*(shadow(v, n, r) for v in zeros))
    assert len(central_shadow) == 1+k*k
    for v in layer(n, r+1):
        if v not in zeros:
            assert len(shadow(v, n, r) & central_shadow) <= 2
    # Root weights in the two nonzero pinned phase contributions.
    low_root = frozenset(range(k-1))
    high_root = frozenset(range(k))
    assert len(shadow(low_root, n, k)) == k+2
    assert len(shadow(high_root, n, k+1)) == k+1


def main():
    for k in range(2, 8):
        right, left = even_coefficients(k)
        odd_geometry(k)
        print(f"k={k}: central={right}, rooted={left}, difference={right-left}; odd geometry PASS")
    print("PASS: local coefficients and geometry; analytic tails require the proof")


if __name__ == "__main__":
    main()
