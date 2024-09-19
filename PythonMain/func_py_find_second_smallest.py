# func_py_find_second_smallest.py
def func_py_find_second_smallest(lst):
    unique_sorted_lst = sorted(set(lst))
    return unique_sorted_lst[1] if len(unique_sorted_lst) >= 2 else None

print(func_py_find_second_smallest([3, 1, 4, 1, 5, 9]))
