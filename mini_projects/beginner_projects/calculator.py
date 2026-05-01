# ⭐ Mini Project 2 — Calculator 🧮

operator = input("Enter an operator (+, -, *, /): ")
num1     = float(input("Enter number 1: "))
num2     = float(input("Enter number 2: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        result = None
    else:
        result = num1 / num2
else:
    print(f"Invalid operator: '{operator}'. Use +, -, *, or /")
    result = None

if result is not None:
    print(f"\nResult: {num1} {operator} {num2} = {round(result, 3)}")
