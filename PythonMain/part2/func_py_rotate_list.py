# func_py_rotate_list.py
def func_py_rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
