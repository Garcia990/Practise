# func_py_check_armstrong_number.py
def func_py_check_armstrong_number(number):
    num_digits = len(str(number))
    return number == sum([int(digit)**num_digits for digit in str(number)])

print(func_py_check_armstrong_number(153))
