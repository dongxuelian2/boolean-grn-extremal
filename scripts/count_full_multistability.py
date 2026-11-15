#!/usr/bin/env python3
"""Exact node-level monotone-Boolean counts for a full single-high-state set.

Setting: n nodes, all-to-all inputs, positive self-loop on distinguished node 0,
and m negative inputs chosen from nodes 1,...,n-1. This is the setting of
Harshavardhan et al. (2026), Section 6.3 / Algorithm 6.12.
"""
from functools import lru_cache
import argparse


def count_models(n: int, m: int, *, pivot: str = "lowest") -> int:
    """Count monotone f: {0,1}^n -> {0,1} satisfying signed-state tests."""
    if n < 2 or n > 7:
        raise ValueError("reference exact enumerator is intentionally limited to 2 <= n <= 7")
    if not 0 <= m < n:
        raise ValueError("m must be in 0..n-1")

    if pivot not in ("lowest", "highest"):
        raise ValueError("pivot must be lowest or highest")

    size = 1 << n
    all_points = (1 << size) - 1
    down = [0] * size
    up = [0] * size
    for x in range(size):
        for y in range(size):
            if (y & x) == y:
                down[x] |= 1 << y
            if (y & x) == x:
                up[x] |= 1 << y

    neg = sum(1 << j for j in range(1, m + 1))
    forced_one = up[neg | 1]  # state e_0 (self-high)
    forced_zero = 0
    for j in range(1, n):
        forced_zero |= down[neg ^ (1 << j)]  # state e_j (other-high)
    if forced_one & forced_zero:
        return 0
    free = all_points & ~(forced_one | forced_zero)

    @lru_cache(None)
    def count(free_mask: int) -> int:
        if not free_mask:
            return 1
        bit = (free_mask & -free_mask) if pivot == "lowest" else (1 << (free_mask.bit_length() - 1))
        x = bit.bit_length() - 1
        # If f(x)=0, every lower point is also zero.
        # If f(x)=1, every upper point is also one.
        return count(free_mask & ~down[x]) + count(free_mask & ~up[x])

    return count(free)


def row(n: int) -> list[int]:
    return [count_models(n, m) for m in range(n)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5, choices=range(2, 8))
    args = parser.parse_args()
    for n in range(2, args.max_n + 1):
        values = row(n)
        best = max(values)
        maximizers = [m for m, v in enumerate(values) if v == best]
        print(f"n={n}: |W(n,m)|={values}; maximizing m={maximizers}")


if __name__ == "__main__":
    main()
