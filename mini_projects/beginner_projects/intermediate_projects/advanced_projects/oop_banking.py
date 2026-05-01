# ⭐ Mini Project 12 — OOP Banking Program 💰

class BankAccount:
    def __init__(self, owner):
        self.owner     = owner
        self.__balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"  ✅ Deposited ₹{amount:,.2f}")
        else:
            print("  Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("  Amount must be positive.")
        elif amount > self.__balance:
            print("  ❌ Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"  ✅ Withdrawn ₹{amount:,.2f}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.owner}] — ₹{self.__balance:,.2f}"


name = input("Enter your name: ")
acc  = BankAccount(name)
print(f"\nAccount created for {name}! 🏦")

while True:
    print("\n── MENU ─────────────────────")
    print("  1. Deposit   2. Withdraw")
    print("  3. Balance   4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        acc.deposit(float(input("Amount: ₹")))
    elif choice == "2":
        acc.withdraw(float(input("Amount: ₹")))
    elif choice == "3":
        print(f"  {acc}")
    elif choice == "4":
        print(f"\nGoodbye, {name}! Final balance: ₹{acc.get_balance():,.2f}")
        break
    else:
        print("  Invalid option.")
