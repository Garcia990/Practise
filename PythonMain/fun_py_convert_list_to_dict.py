# fun_py_convert_list_to_dict.py
def fun_py_convert_list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

print(fun_py_convert_list_to_dict([10, 20, 30, 40]))
