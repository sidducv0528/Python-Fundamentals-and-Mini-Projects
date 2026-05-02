# ⭐ Bonus Mini Project — Number Guessing Game 🎲

import random

secret   = random.randint(1, 100)
attempts = 0

print("🎯 Guess the number between 1 and 100!")

while True:
    guess    = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("📉 Too low! Try higher.")
    elif guess > secret:
        print("📈 Too high! Try lower.")
    else:
        print(f"🎉 Correct! The number was {secret}.")
        print(f"   You got it in {attempts} attempt(s)!")
        break
