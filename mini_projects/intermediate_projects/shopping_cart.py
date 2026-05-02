# ⭐ Mini Project 7 — Shopping Cart 🛒
# Track multiple items and quantities with parallel lists.

foods  = []
prices = []

while True:
    item = input("Enter a food item (or 'q' to quit): ")
    if item.lower() == "q":
        break

    price    = float(input(f"Price of {item}: $"))
    quantity = int(input(f"Quantity of {item}: "))

    foods.append(item)
    prices.append(price * quantity)

total = sum(prices)

print("\n" + "─" * 40)
print("           YOUR CART")
print("─" * 40)
for i in range(len(foods)):
    print(f"{foods[i]:<20} ${prices[i]:>8.2f}")
print("─" * 40)
print(f"{'Grand Total':<20} ${total:>8,.2f}")
