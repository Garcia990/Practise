# func_py_calculate_geometric_mean.py
import math

def func_py_calculate_geometric_mean(numbers):
    product = math.prod(numbers)
    return product ** (1 / len(numbers))

print(func_py_calculate_geometric_mean([1, 2, 3, 4, 5]))
