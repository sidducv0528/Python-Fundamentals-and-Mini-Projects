# ⭐ Mini Project 14 — Encryption Program 🔐
# A simple substitution cipher — maps every character to a random shuffled key.

import random
import string

# Build character set and shuffled key
chars = list(string.ascii_letters + string.digits +
             string.punctuation + string.whitespace)
key   = chars.copy()
random.shuffle(key)

# ENCRYPT
message   = input("Enter a message to encrypt: ")
encrypted = "".join(key[chars.index(ch)] for ch in message)

print(f"\n🔒 Encrypted : {encrypted}")
print(f"📝 Original  : {message}")

# DECRYPT
secret_code = input("\nEnter the secret code to decrypt: ")
decrypted   = "".join(chars[key.index(ch)] for ch in secret_code)

print(f"🔓 Decrypted : {decrypted}")
