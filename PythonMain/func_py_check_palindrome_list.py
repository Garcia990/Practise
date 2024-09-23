# func_py_check_palindrome_list.py
def func_py_check_palindrome_list(lst):
    return lst == lst[::-1]

print(func_py_check_palindrome_list([1, 2, 3, 2, 1]))
