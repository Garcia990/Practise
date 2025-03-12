# func_py_bmi_calculator.py
def func_py_bmi_calculator(weight, height):
    if height <= 0:
        return "Invalid height"
    bmi = weight / (height ** 2)
    category = "Underweight" if bmi < 18.5 else "Normal" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
    return f"BMI: {bmi:.2f}, Category: {category}"

print(func_py_bmi_calculator(70, 1.75))
