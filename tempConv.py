""" Temperature unit converter 
import numpy as np

temperatures = input("Enter temperature:").split(",")
temperatures = np.array([float(t) for t in temperatures])

current_unit = input("Current Unit (C/F/K): ").upper()
target_unit = input("Target unit (C/F/K): ").upper()

if current_unit == "C" and target_unit == "F":
    converted = temperatures * 9/5 + 32
elif current_unit == "C" and target_unit == "K":
    converted = temperatures + 273.15
elif current_unit == "F" and target_unit == "K":
    converted = (temperatures - 32) * 5/9 * 273.15
elif current_unit == "K" and target_unit == "C":
    converted = temperatures - 273.15
elif current_unit == "K" and target_unit == "F":
    converted = (temperatures - 273.15) * 9/5 + 32
else:
    print("Invalid unit")
    exit()

print(f"Converted temperatures ({target_unit}) = ({converted})")
"""
