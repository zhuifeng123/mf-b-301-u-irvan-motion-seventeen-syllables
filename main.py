#!/usr/bin/env python3
import os

def main():
    os.makedirs("/output", exist_ok=True)
    haiku = "Code breaks at midnight\nStack trace reveals the error\nFix committed, tests pass"
    with open("/output/entry.txt", "w") as f:
        f.write(haiku)

if __name__ == "__main__":
    main()