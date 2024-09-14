# func_py_find_longest_word.py
def func_py_find_longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest

print(func_py_find_longest_word("Python is a programming language"))
