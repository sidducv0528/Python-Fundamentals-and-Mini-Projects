# ⭐ Mini Project 8 — Quiz Game 💯
# Uses tuples (immutable) for questions, options, and answers.

questions = (
    "1. How many elements are in the periodic table?",
    "2. Which animal lays the largest eggs?",
    "3. What is the hardest natural substance on Earth?",
    "4. What is the largest mammal in the world?",
    "5. Which planet is known as the Red Planet?",
)

options = (
    ("A. 115", "B. 117", "C. 118", "D. 121"),
    ("A. Whale", "B. Ostrich", "C. Kangaroo", "D. Anaconda"),
    ("A. Ruby", "B. Gold", "C. Diamond", "D. Iron"),
    ("A. Blue Whale", "B. Octopus", "C. Jellyfish", "D. Shark"),
    ("A. Sun", "B. Neptune", "C. Mercury", "D. Mars"),
)

answers = ("C", "B", "C", "A", "D")
guesses = []
score   = 0

for i, question in enumerate(questions):
    print("─" * 45)
    print(question)
    for option in options[i]:
        print(f"   {option}")
    guess = input("Your answer (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        score += 1
        print("✅ CORRECT!")
    else:
        print(f"❌ WRONG! The answer was: {answers[i]}")

print("\n" + "═" * 45)
print(f"  Score      : {score} / {len(questions)}")
print(f"  Percentage : {(score / len(questions)) * 100:.1f}%")
print(f"  Your answers   : {guesses}")
print(f"  Correct answers: {list(answers)}")
