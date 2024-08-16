# func_py_calculate_torus_volume.py
import math

def func_py_calculate_torus_volume(major_radius, minor_radius):
    return (math.pi * minor_radius**2) * (2 * math.pi * major_radius)

print(func_py_calculate_torus_volume(7, 2))
