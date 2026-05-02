# ⭐ Mini Project 11 — Personal Diary App 📔
# Uses File I/O to save and load diary entries that persist between runs!

from datetime import datetime

DIARY_FILE = "my_diary.txt"

def write_entry(entry):
    """Append a timestamped entry to the diary."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DIARY_FILE, "a") as file:
        file.write(f"\n{'─' * 45}\n")
        file.write(f"📅 {timestamp}\n")
        file.write(f"{entry}\n")
    print("✅ Entry saved!")

def read_diary():
    """Read and print all diary entries."""
    try:
        with open(DIARY_FILE, "r") as file:
            content = file.read()
        print("\n📔 My Diary:")
        print(content if content.strip() else "Diary is empty. Start writing!")
    except FileNotFoundError:
        print("No diary yet. Write your first entry!")

def count_entries():
    try:
        with open(DIARY_FILE, "r") as file:
            count = sum(1 for line in file if line.startswith("📅"))
        print(f"Total entries: {count}")
    except FileNotFoundError:
        print("No diary file found.")

# Main menu
while True:
    print("\n── DIARY MENU ──────────────────")
    print("  1. Write new entry")
    print("  2. Read all entries")
    print("  3. Count entries")
    print("  4. Exit")

    choice = input("Choose: ")
    if choice == "1":
        entry = input("Write your entry:\n> ")
        write_entry(entry)
    elif choice == "2":
        read_diary()
    elif choice == "3":
        count_entries()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice.")
