# ⭐ Mini Project 6 — Countdown Timer ⏱️

import time

seconds = int(input("Enter countdown seconds: "))

for x in range(seconds, 0, -1):
    hh = x // 3600
    mm = (x % 3600) // 60
    ss = x % 60
    print(f"\r⏳ {hh:02}:{mm:02}:{ss:02}", end="", flush=True)
    time.sleep(1)

print("\n🔔 Time's up!")
