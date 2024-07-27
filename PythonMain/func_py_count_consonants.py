# func_py_count_consonants.py
def func_py_count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in string if char in consonants)

print(func_py_count_consonants("Hello, World!"))
