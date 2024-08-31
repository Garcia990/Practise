# func_py_calculate_bicorn_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_bicorn_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.sin(t)
    y = a * (1 + np.cos(t)) *
