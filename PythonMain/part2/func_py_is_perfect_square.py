# func_py_is_perfect_square.py

import math

def func_py_is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

def test_perfect_square():
    numbers = [4, 16, 23, 25, 36, 49]
    for num in numbers:
        print(f"{num} is a perfect square: {func_py_is_perfect_square(num)}")

if __name__ == "__main__":
    test_perfect_square()
