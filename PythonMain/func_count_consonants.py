# func_count_consonants.py
def func_count_consonants(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char.isalpha() and char not in vowels)

print(func_count_consonants("Hello World"))
