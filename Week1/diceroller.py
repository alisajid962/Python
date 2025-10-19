import random

dice_numbers = [1, 2, 3, 4, 5, 6]
is_playing = True

while is_playing:
    roll = input("Roll the dice (y/n): ").strip().lower()

    if roll == 'y':
        dice = random.choice(dice_numbers)
        print("-------------------")
        print(f"You rolled: {dice}")
        print("-------------------")

    elif roll == 'n':
        print("Thanks for playing!")
        is_playing = False

    else:
        print("Invalid input! Please enter 'y' or 'n'.")
