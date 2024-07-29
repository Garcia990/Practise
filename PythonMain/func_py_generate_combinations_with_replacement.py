# func_py_generate_combinations_with_replacement.py
from itertools import combinations_with_replacement

def func_py_generate_combinations_with_replacement(lst, r):
    return list(combinations_with_replacement(lst, r))

print(func_py_generate_combinations_with_replacement([1, 2, 3], 2))
