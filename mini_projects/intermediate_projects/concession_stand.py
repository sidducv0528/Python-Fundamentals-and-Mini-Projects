# ⭐ Mini Project 9 — Concession Stand 🍿
# Combines dictionaries, while loops, and nested menus.

tiffin_menu = {
    "idli" : 35,
    "vada" : 35,
    "dosa" : 40,
    "poha" : 30,
    "upma" : 30,
}

meal_menu = {
    "veg_biryani"     : 150,
    "chicken_biryani" : 200,
    "mutton_biryani"  : 250,
    "fish_biryani"    : 200,
}

cart  = []
total = 0

while True:
    print("\n[T] Tiffins  [M] Meals  [Q] Quit & Pay")
    category = input("Select category: ").lower()

    if category == "q":
        break
    elif category == "t":
        menu, label = tiffin_menu, "TIFFIN"
    elif category == "m":
        menu, label = meal_menu, "MEALS"
    else:
        print("Invalid. Use T, M, or Q.")
        continue

    while True:
        print(f"\n── {label} MENU ──")
        for item, price in menu.items():
            print(f"  {item:<20} ₹{price}")
        order = input("Item (or 'done'): ").lower()
        if order == "done":
            break
        if order in menu:
            cart.append({"name": order, "price": menu[order]})
            total += menu[order]
            print(f"  '{order}' added! ✅")
        else:
            print("  Item not found. Check the menu.")

print("\n" + "─" * 40)
if cart:
    for entry in cart:
        print(f"{entry['name']:<25} ₹{entry['price']:.2f}")
    print(f"\n{'Grand Total':<25} ₹{total:.2f}")
else:
    print("Your cart is empty.")
