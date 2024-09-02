# func_py_generate_binomial_coefficients.py
def func_py_generate_binomial_coefficients(n):
    coeffs = [1]
    for k in range(1, n + 1):
        coeffs.append(coeffs[-1] * (n - k + 1) // k)
    return coeffs

print(func_py_generate_binomial_coefficients(5))
