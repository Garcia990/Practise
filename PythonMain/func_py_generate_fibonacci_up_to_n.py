# func_py_generate_fibonacci_up_to_n.py
def func_py_generate_fibonacci_up_to_n(n):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

print(func_py_generate_fibonacci_up_to_n(50))
