# fun_py_find_vowel_occurrences.py
def fun_py_find_vowel_occurrences(string):
    vowels = "aeiouAEIOU"
    return {char: string.count(char) for char in vowels if char in string}

print(fun_py_find_vowel_occurrences("banana"))
