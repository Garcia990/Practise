# func_py_sort_dict_by_values.py
def func_py_sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

print(func_py_sort_dict_by_values({'apple': 2, 'banana': 4, 'orange': 1}))
