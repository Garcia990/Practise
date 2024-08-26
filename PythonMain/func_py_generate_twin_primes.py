# func_py_generate_twin_primes.py
def func_py_generate_twin_primes(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    return [(n, n+2) for n in range(2, limit) if is_prime(n) and is_prime(n + 2)]

print(func_py_generate_twin_primes(100))
