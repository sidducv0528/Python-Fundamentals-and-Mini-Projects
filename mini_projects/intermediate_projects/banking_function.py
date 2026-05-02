# ⭐ Mini Project 10 — Banking Program 💰 (Function-Based)
# Demonstrates functions working together with a shared state variable.

balance = 0

def show_balance(bal):
    print(f"\n  💰 Balance: ${bal:,.2f}")

def deposit():
    amount = float(input("  Amount to deposit: $"))
    if amount <= 0:
        print("  ❌ Invalid amount.")
        return 0
    return amount

def withdraw(current_balance):
    amount = float(input("  Amount to withdraw: $"))
    if amount <= 0:
        print("  ❌ Invalid amount.")
        return 0
    if amount > current_balance:
        print("  ❌ Insufficient funds!")
        return 0
    return amount

while True:
    print("\n── MENU ──────────────────────")
    print("  1. Show Balance")
    print("  2. Deposit")
    print("  3. Withdraw")
    print("  4. Exit")

    choice = input("  Choose: ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw(balance)
    elif choice == "4":
        show_balance(balance)
        print("  Goodbye! 👋")
        break
    else:
        print("  Invalid choice.")
