# func_py_calculate_sum_of_cubes.py
def func_py_calculate_sum_of_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

print(func_py_calculate_sum_of_cubes(3))