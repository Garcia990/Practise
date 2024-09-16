# func_py_find_armstrong_numbers_in_range.py
def func_py_find_armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        digits = list(map(int, str(num)))
        if num == sum([digit ** len(digits) for digit in digits]):
            armstrong_numbers.append(num)
    return armstrong_numbers

print(func_py_find_armstrong_numbers_in_range(100, 1000))
