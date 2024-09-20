# func_py_check_anagrams.py
def func_py_check_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(func_py_check_anagram("listen", "silent"))
