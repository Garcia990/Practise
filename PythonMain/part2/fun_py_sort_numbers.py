# fun_py_sort_numbers.py

def fun_py_sort_numbers(lst):
    return sorted(lst)

def test_sort_numbers():
    numbers = [5, 2, 8, 1, 3]
    print(f"Sorted numbers: {fun_py_sort_numbers(numbers)}")

if __name__ == "__main__":
    test_sort_numbers()
