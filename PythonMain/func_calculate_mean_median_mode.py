# func_calculate_mean_median_mode.py
from statistics import mean, median, mode

def func_calculate_mean_median_mode(lst):
    return {
        'mean': mean(lst),
        'median': median(lst),
        'mode': mode(lst)
    }

print(func_calculate_mean_median_mode([1, 2, 3, 4, 4, 5, 5, 5]))
