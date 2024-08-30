# func_py_calculate_epispiral_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_epispiral_curve(a, n, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.cos(t)**n
    y = a * np.sin(t)**n
    plt.plot(x, y)
    plt.title("Epispiral Curve")
    plt.show()

func_py_calculate_epispiral_curve(5, 2, 1000)
