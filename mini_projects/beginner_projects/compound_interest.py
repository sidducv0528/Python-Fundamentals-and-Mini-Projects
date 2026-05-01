# ⭐ Mini Project 5 — Compound Interest Calculator 💵
# Formula: A = P(1 + r/100)^t

principal = float(input("Enter the principal amount ($): "))
while principal < 0:
    print("Principal cannot be negative.")
    principal = float(input("Enter the principal amount ($): "))

rate = float(input("Enter the annual interest rate (%): "))
while rate < 0:
    print("Rate cannot be negative.")
    rate = float(input("Enter the annual interest rate (%): "))

time = float(input("Enter the time period (years): "))
while time < 0:
    print("Time cannot be negative.")
    time = float(input("Enter the time period (years): "))

total    = principal * (1 + rate / 100) ** time
interest = total - principal

print("\n" + "─" * 45)
print(f"  Principal    : ${principal:>12,.2f}")
print(f"  Rate         : {rate:>12}%")
print(f"  Time         : {time:>12} years")
print("─" * 45)
print(f"  Interest     : ${interest:>12,.2f}")
print(f"  Total Amount : ${total:>12,.2f}")
print("─" * 45)
