import math
import unittest
import random

def wallis(n):
    product = 1
    while n != 0:
        product = product*(4*n*n)/(4*n*n-1)
        n = n-1
    return 2*product
def monte_carlo(n):
    circle_pointes = 0
    square_points = 0
    while n != 0:
        a = random.random()
        b = random.random()
        val = a**2+b**2
        if val <= 1:
            circle_pointes  = circle_pointes + 1
        else:
            square_points = square_points + 1
        n = n - 1    
    ratio = circle_pointes/(circle_pointes + square_points)
    return 4*ratio

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
