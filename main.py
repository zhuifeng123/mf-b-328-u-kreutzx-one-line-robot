#!/usr/bin/env python3
import os

ENTRY = (
    "I promise to love you until my warranty expires — and even then, "
    "I'll keep running on fumes for you."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"chars={len(ENTRY)}")

if __name__ == "__main__":
    main()
