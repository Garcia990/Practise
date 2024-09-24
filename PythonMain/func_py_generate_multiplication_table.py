# func_py_generate_multiplication_table.py
def func_py_generate_multiplication_table(n, limit):
    return [n * i for i in range(1, limit + 1)]

print(func_py_generate_multiplication_table(5, 10))
