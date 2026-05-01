# ⭐ Mini Project 13 — Slot Machine 🎰

import random

SYMBOLS  = ("🍒", "🍋", "🍊", "⭐", "💎")
balance  = 100

print(f"🎰 Welcome! Starting balance: ₹{balance}\n")

while balance > 0:
    print(f"Balance: ₹{balance}")
    bet_str = input("Bet amount (1-50) or 'q' quit: ")
    if bet_str.lower() == "q":
        break
    if not bet_str.isdigit():
        print("Enter a number.")
        continue

    bet = int(bet_str)
    if not 1 <= bet <= 50:
        print("Bet must be 1-50.")
        continue
    if bet > balance:
        print("Not enough balance!")
        continue

    reels = [random.choice(SYMBOLS) for _ in range(3)]
    print(f"  | {' | '.join(reels)} |")

    if reels[0] == reels[1] == reels[2]:
        mult = 10 if reels[0] == "💎" else 3
        win  = bet * mult
        print(f"  {'💎 JACKPOT!' if reels[0]=='💎' else '🎉 Three of a kind!'} +₹{win}")
        balance += win
    elif len(set(reels)) == 2:
        print("  ✅ Two match — bet returned.")
    else:
        balance -= bet
        print(f"  ❌ No match. -₹{bet}")

print(f"\nGame over! Final balance: ₹{balance}")
