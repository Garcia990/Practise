# func_py_calculate_cylinder_surface_area_with_top_bottom.py
import math

def func_py_calculate_cylinder_surface_area_with_top_bottom(radius, height):
    return 2 * math.pi * radius * (radius + height)

print(func_py_calculate_cylinder_surface_area_with_top_bottom(3, 5))
