# func_py_calculate_sphere_surface_to_volume_ratio.py
import math

def func_py_calculate_sphere_surface_to_volume_ratio(radius):
    surface_area = 4 * math.pi * radius**2
    volume = (4/3) * math.pi * radius**3
    return surface_area / volume

print(func_py_calculate_sphere_surface_to_volume_ratio(3))
