# ⭐ Mini Project 4 — Temperature Converter 🌡️

temperature = float(input("Enter the temperature: "))
unit        = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    converted = (temperature * 9 / 5) + 32
    print(f"{temperature}°C = {round(converted, 2)}°F")
elif unit == "F":
    converted = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {round(converted, 2)}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
