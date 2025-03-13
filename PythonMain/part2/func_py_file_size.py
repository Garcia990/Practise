# func_py_file_size.py
import os

def func_py_file_size(filename):
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        return "File not found"

print(func_py_file_size("example.txt"))
