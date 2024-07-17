# func_find_all_permutations.py
from itertools import permutations

def func_find_all_permutations(lst):
    return list(permutations(lst))

print(func_find_all_permutations([1, 2, 3]))
