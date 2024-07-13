# func_fibonacci_recursive.py
def func_fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return func_fibonacci_recursive(n-1) + func_fibonacci_recursive(n-2)

print(func_fibonacci_recursive(10))
