import timeit
from euclidgcd import gcd_euclid

def test_gcd_euclid():
    assert gcd_euclid(1200, 64) == 16
    assert gcd_euclid(48, 9) == 3
    assert gcd_euclid(685, 45) == 5

test_gcd_euclid()

print("Euclid Test Passed")
print("Execution time: ", timeit.timeit(test_gcd_euclid, number=1000), "seconds")
