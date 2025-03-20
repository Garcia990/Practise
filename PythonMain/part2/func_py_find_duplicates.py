# func_py_find_duplicates.py

def func_py_find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

def test_find_duplicates():
    data = [1, 2, 3, 4, 5, 2, 3, 7, 8]
    print(f"Duplicates: {func_py_find_duplicates(data)}")

if __name__ == "__main__":
    test_find_duplicates()
