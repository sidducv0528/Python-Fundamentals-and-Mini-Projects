# ⭐ Bonus Mini Project — Rock Paper Scissors ✊✋✌️

import random

choices        = ["rock", "paper", "scissors"]
wins           = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
player_score   = 0
computer_score = 0
rounds         = 0

print("🎮 Rock Paper Scissors — best of 3!")

while rounds < 3:
    player   = input("\nEnter rock, paper, or scissors: ").lower()
    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("🤝 It's a tie!")
    elif wins[player] == computer:
        print("✅ You win this round!")
        player_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    rounds += 1

print(f"\n📊 Final Score — You: {player_score}  |  Computer: {computer_score}")
if player_score > computer_score:
    print("🏆 You won the game!")
elif computer_score > player_score:
    print("💻 Computer won the game!")
else:
    print("🤝 It's a draw!")
