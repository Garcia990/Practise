# func_py_generate_hyperbolic_numbers.py
def func_py_generate_hyperbolic_numbers(n):
    return [i * (i + 1) for i in range(1, n + 1)]

print(func_py_generate_hyperbolic_numbers(10))
