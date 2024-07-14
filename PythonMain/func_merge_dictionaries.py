# func_merge_dictionaries.py
def func_merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

print(func_merge_dictionaries({'a': 1}, {'b': 2}))
