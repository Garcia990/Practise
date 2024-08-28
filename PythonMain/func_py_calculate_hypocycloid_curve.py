# func_py_calculate_hypocycloid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_hypocycloid_curve(radius1, radius2, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = (radius1 - radius2) * np.cos(t) + radius2 * np.cos((radius1 - radius2) * t / radius2)
    y = (radius1 - radius2) * np.sin(t) - radius2 * np.sin((radius1 - radius2) * t / radius2)
    plt.plot(x, y)
    plt.title("Hypocycloid Curve")
    plt.show()

func_py_calculate_hypocycloid_curve(5, 3, 1000)
