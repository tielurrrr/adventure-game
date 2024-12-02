from chapter_three import chapter_three

def chapter_two(character):
    """Chapter 2: The Mines"""
    print("\n--- Chapter 2: The Mines ---")
    print("The group enters the dark, damp mines. The air is thick, and the sound of distant growls fills the space.")
    print("Suddenly, monsters appear, and you must act quickly!")

    while True:
        print("\nWhat will you do?")
        print("1. Charge in alone.")
        print("2. Support and fight with the team.")
        print("3. Run away.")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            print("\nYou charge in recklessly. The monsters overwhelm you, and your entire team suffers injuries.")
            print("The team scolds you for your rash decision. Try again.")
        elif choice == "2":
            print("\nYou fight strategically alongside your team, combining your strengths.")
            print("Together, you defeat the monsters and secure the mine!")
            print("Your team cheers for your bravery and teamwork.")
            print("Congratulations, you completed the quest successfully!")
            chapter_three(character)
            break
        elif choice == "3":
            print("\nYou run away, leaving your team to fight alone. The monsters overpower them.")
            print("Your team perishes, and the quest ends in failure.")
            print("Try to make a better choice next time.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
