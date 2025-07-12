#!/usr/bin/env python3
import random
import subprocess
from pathlib import Path

# Read jokes from jokes.txt
jokes_file = Path.home() / ".config/kitty/jokes.txt"
try:
    with jokes_file.open(encoding="utf-8") as f:
        jokes = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    jokes = ["No jokes file found at ~/.config/kitty/jokes.txt"]

def get_cowsay_animals():
    try:
        output = subprocess.check_output(['cowsay', '-l'], text=True)
        lines = output.strip().split('\n')
        animals = ' '.join(lines[1:]).split()
        return animals
    except Exception:
        return ["default"]

# Pick random joke and animal
joke = random.choice(jokes)
animals = get_cowsay_animals()
animal = random.choice(animals)

# Use cowsay with the selected animal and joke
try:
    output = subprocess.check_output(['cowsay', '-f', animal, joke], text=True)
    print(output)
except subprocess.CalledProcessError as e:
    print("Error running cowsay:", e)
except FileNotFoundError:
    print("🐄 'cowsay' is not installed. Please install it with `sudo apt install cowsay` or similar.")
