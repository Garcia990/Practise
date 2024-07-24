# fun_py_calculate_cylinder_surface_area.py
import math

def fun_py_calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

print(fun_py_calculate_cylinder_surface_area(3, 5))
