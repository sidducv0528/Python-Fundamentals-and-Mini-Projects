# ⭐ Mini Project 3 — Weight Converter 🏋️

weight = float(input("Enter your weight: "))
unit   = input("Enter unit — K for kilograms, L for pounds: ").upper()

if unit == "K":
    converted = weight * 2.2046
    print(f"{weight} kg = {round(converted, 2)} pounds")
elif unit == "L":
    converted = weight / 2.2046
    print(f"{weight} lbs = {round(converted, 2)} kg")
else:
    print("Invalid unit. Please enter 'K' or 'L'.")
