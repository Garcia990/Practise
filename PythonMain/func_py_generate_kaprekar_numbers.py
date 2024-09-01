# func_py_generate_kaprekar_numbers.py
def func_py_generate_kaprekar_numbers(limit):
    kaprekar_numbers = []
    for n in range(1, limit + 1):
        sq_n = n**2
        str_n = str(sq_n)
        for i in range(1, len(str_n)):
            left, right = int(str_n[:i]), int(str_n[i:])
            if right > 0 and left + right == n:
                kaprekar_numbers.append(n)
                break
    return kaprekar_numbers

print(func_py_generate_kaprekar_numbers(1000))
