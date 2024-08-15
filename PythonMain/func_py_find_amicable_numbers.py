# func_py_find_amicable_numbers.py
def func_py_find_amicable_numbers(limit):
    amicable_pairs = []
    for num in range(2, limit):
        sum_div1 = sum([i for i in range(1, num) if num % i == 0])
        sum_div2 = sum([i for i in range(1, sum_div1) if sum_div1 % i == 0])
        if sum_div2 == num and num != sum_div1:
            amicable_pairs.append((num, sum_div1))
    return amicable_pairs

print(func_py_find_amicable_numbers(10000))
