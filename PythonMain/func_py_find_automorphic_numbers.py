# func_py_find_automorphic_numbers.py
def func_py_find_automorphic_numbers(limit):
    return [i for i in range(limit) if str(i**2).endswith(str(i))]

print(func_py_find_automorphic_numbers(100))
