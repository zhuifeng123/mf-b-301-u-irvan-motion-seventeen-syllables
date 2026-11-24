#!/usr/bin/env python3
import os

def main():
    os.makedirs("/output", exist_ok=True)
    haiku = "Breakpoint hits hard\nVariable reveals the lie\nCode breathes again"
    with open("/output/entry.txt", "w") as f:
        f.write(haiku)

if __name__ == "__main__":
    main()