# func_py_caesar_cipher.py

def func_py_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr(shift_base + (ord(char) - shift_base + shift) % 26)
        else:
            result += char
    return result

def test_caesar_cipher():
    print(func_py_caesar_cipher("Hello World!", 3))

if __name__ == "__main__":
    test_caesar_cipher()
