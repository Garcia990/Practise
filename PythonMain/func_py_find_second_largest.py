# func_py_find_second_largest.py
def func_py_find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

print(func_py_find_second_largest([10, 20, 20, 40, 50]))
