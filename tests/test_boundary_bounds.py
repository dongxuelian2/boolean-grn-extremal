"""Check derived ranks independently against original signed-state constraints."""
import unittest
from math import comb
from fractions import Fraction
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from count_full_multistability import count_models
from boundary_bounds import (free_rank, lower_log2,
    inhibitory_boundary_coefficient, activating_boundary_coefficient)


def direct_free(n, m):
    z = sum(1 << j for j in range(1, m + 1))
    positive = z | 1
    negative = [z ^ (1 << j) for j in range(1, n)]
    return [x for x in range(1 << n)
            if x & positive != positive and not any(x & y == x for y in negative)]


class BoundaryBounds(unittest.TestCase):
    def test_all_ranks_against_signed_constraints(self):
        for n in range(2, 11):
            for m in range(n):
                actual = [0] * (n + 1)
                for x in direct_free(n, m):
                    actual[x.bit_count()] += 1
                self.assertEqual([free_rank(n,m,r) for r in range(n+1)], actual)

    def test_lower_bound_and_slice_upper_bounds(self):
        D = [2, 3, 6, 20, 168, 7581]
        for n in range(2, 6):
            for m in range(n):
                a = n - 1 - m
                C = count_models(n, m)
                self.assertLessEqual(2**lower_log2(n,m), C)
                self.assertLessEqual(C, D[a]**(2**(m+1)-1))
                if a:
                    self.assertLessEqual(C, D[m]**(2**(a+1)-a-1))
                else:
                    self.assertEqual(C, 2*(D[m]-1))

    def test_balanced_exact_middle_layer(self):
        for n in range(4, 101):
            r=n//2; a=n-1-r
            self.assertEqual(free_rank(n,r,r),comb(n,r)-1-a*r)

    def test_fixed_boundary_coefficients(self):
        self.assertEqual(inhibitory_boundary_coefficient(1),Fraction(3,4))
        self.assertEqual(activating_boundary_coefficient(0),Fraction(1,2))
        self.assertEqual(activating_boundary_coefficient(1),Fraction(1,2))
        self.assertEqual(activating_boundary_coefficient(2),Fraction(5,8))

    def test_invalid(self):
        for args in [(1,0,0),(3,3,0),(3,-1,0),(3,1,4)]:
            with self.assertRaises(ValueError): free_rank(*args)




class UniformBounds(unittest.TestCase):
    def test_uniform_middle_loss(self):
        from boundary_bounds import uniform_middle_loss
        for n in range(2,101):
            for m in range(n-1):
                fraction=Fraction(free_rank(n,m,n//2),comb(n,n//2))
                self.assertGreaterEqual(fraction, 1-uniform_middle_loss(n,m))

    def test_central_ratio_product(self):
        from boundary_bounds import central_ratio
        for n in range(2,101):
            for h in range(n):
                product=Fraction(1)
                for d in range(n-h+1,n+1):
                    product*=Fraction(d+1,d) if d%2 else 1
                self.assertEqual(central_ratio(n,h),product)
                self.assertGreaterEqual(product,1)
                self.assertLessEqual(product,Fraction(n-h+2,n-h+1)**h)

    def test_invalid_uniform_inputs(self):
        from boundary_bounds import uniform_middle_loss, central_ratio
        for args in [(1,0),(3,-1),(3,2)]:
            with self.assertRaises(ValueError): uniform_middle_loss(*args)
        for args in [(0,0),(3,-1),(3,3)]:
            with self.assertRaises(ValueError): central_ratio(*args)

if __name__ == '__main__':
    unittest.main()
