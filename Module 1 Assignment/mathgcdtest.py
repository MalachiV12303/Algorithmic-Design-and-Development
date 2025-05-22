import timeit
from mathgcd import gcd_math

def test_gcd_math():
    assert gcd_math(1200, 64) == 16
    assert gcd_math(48, 9) == 3
    assert gcd_math(685, 45) == 5

test_gcd_math()

print("Math Library GCD Test")
print("Execution time: ", timeit.timeit(test_gcd_math, number=1000), "seconds")
