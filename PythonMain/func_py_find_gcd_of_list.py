# func_py_find_gcd_of_list.py
import math

def func_py_find_gcd_of_list(lst):
    gcd_val = lst[0]
    for num in lst[1:]:
        gcd_val = math.gcd(gcd_val, num)
    return gcd_val

print(func_py_find_gcd_of_list([54, 24, 36]))
