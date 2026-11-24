#!/usr/bin/env python3
import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write("Breakpoint hits at dawn\nConsole speaks in red error\nCode breathes once again")