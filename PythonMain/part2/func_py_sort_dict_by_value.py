# func_py_sort_dict_by_value.py

def func_py_sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

def test_sort_dict_by_value():
    data = {'apple': 3, 'banana': 1, 'cherry': 2}
    print(f"Sorted dictionary: {func_py_sort_dict_by_value(data)}")

if __name__ == "__main__":
    test_sort_dict_by_value()
