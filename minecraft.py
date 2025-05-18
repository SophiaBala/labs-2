from lab7 import finite_automaton_search
import random

with open("receipts.txt", "r") as file:
    lines = file.readlines()

items = {}
for line in lines:
    if ':' in line:
        name, materials = line.strip().split(":", 1)
        items[name.strip().lower()] = [m.strip().lower() for m in materials.split(",")]

item_name = list(items.keys())

print("Type 'exit' to leave the game.\n")


while True:
    user_item = random.choice(item_name)
    print(user_item)

    matched = finite_automaton_search(lines, user_item)

    correct_item_line = matched[0]
    correct_item_name, materials_str = correct_item_line.strip().split(":", 1)
    correct_materials = [m.strip().lower() for m in materials_str.split(",")]

    user_guess = input("Enter materials separated by commas: ").strip().lower()
    guessed_materials = [m.strip() for m in user_guess.split(",")]

    if user_guess == "exit":
        print("Goodbye!")
        break

    correct = [m for m in guessed_materials if m in correct_materials]
    wrong = [m for m in guessed_materials if m not in correct_materials]

    if not wrong and len(correct) == len(correct_materials):
        print("Nerd ^-^")

    for de in correct_materials:
        if de in correct_materials and de not in guessed_materials:
            print(f"A де {de}?")

    print(f"Wrong guesses: {', '.join(wrong) if wrong else 'None'}\n")

