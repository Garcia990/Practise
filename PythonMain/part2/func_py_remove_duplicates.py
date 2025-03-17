# func_py_remove_duplicates.py

def func_py_remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def test_remove_duplicates():
    items = ["apple", "banana", "apple", "orange", "banana"]
    print(f"Unique items: {func_py_remove_duplicates(items)}")

if __name__ == "__main__":
    test_remove_duplicates()
