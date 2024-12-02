from chapter_twelve import chapter_twelve

def chapter_eleven(character):
    """Chapter 11: Fight with the Sorcerer"""
    print("\n--- Chapter 11: Fight with the Sorcerer ---")
    print("The sorcerer raises their hands, summoning dark magic. The air crackles with energy.")
    print(f"With the {character['artifact']} in your possession, you prepare for a dangerous battle.")
    print("The sorcerer launches a powerful blast of magic straight at you!")

    while True:
        print("\nWhat will you do?")
        print("1. Run and try to find cover.")
        print("2. Dodge the attack.")
        print("3. Block the attack.")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            print("\n--- Running for Cover ---")
            print("You turn and try to find cover, but the sorcerer's magic is too fast.")
            print("The blast hits you squarely, and you collapse to the ground.")
            print("Your journey ends here. The artifact falls into the sorcerer's hands.")
            print("Game Over.")
            break
        elif choice == "2":
            print("\n--- Dodging the Attack ---")
            print("You swiftly dodge the sorcerer's magic, rolling to the side.")
            print(f"Using your {character['gear']}, you counterattack with precision.")
            print("The sorcerer is struck and falls, defeated.")
            victory(character)
            break
        elif choice == "3":
            block_attack(character)
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def block_attack(character):
    """Handle blocking the sorcerer's magic."""
    print("\n--- Blocking the Attack ---")
    if character.get('gear') == "Legendary Elven Armor":
        print("You raise your elven armor, and its magic absorbs the sorcerer's attack!")
        print("The sorcerer looks shocked as you counterattack with a decisive blow.")
        print("The sorcerer is defeated, and the artifact is safe in your hands.")
        victory(character)
    else:
        print("You attempt to block the attack, but without magical protection, the blast overpowers you.")
        print("You are struck down, and the sorcerer takes the artifact.")
        print("Game Over.")


def victory(character):
    """Victory sequence after defeating the sorcerer."""
    print("\n--- Victory ---")
    print("With the sorcerer defeated, you retrieve the artifact and secure it in your belongings.")
    print("The ruin grows unstable, and you quickly make your way out.")
    print("Back at the port, you board a ship and begin your journey back to the capital.")
    print("The artifact's immense power hums softly as you sail away, wondering what challenges lie ahead.")
    chapter_twelve(character)
