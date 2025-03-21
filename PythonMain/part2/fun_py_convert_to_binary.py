# fun_py_convert_to_binary.py

def fun_py_convert_to_binary(n):
    return bin(n)[2:]

def test_convert_to_binary():
    numbers = [5, 10, 15, 20]
    for num in numbers:
        print(f"Binary of {num}: {fun_py_convert_to_binary(num)}")

if __name__ == "__main__":
    test_convert_to_binary()
