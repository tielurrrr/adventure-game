from chapter_four import chapter_four

def chapter_three(character):
    """Chapter 3: Invitation to the Capital"""
    print("\n--- Chapter 3: Invitation to the Capital ---")
    print("After your success in the mines, word of your bravery spreads quickly.")
    print("The adventurers are impressed and invite you to travel with them to the capital.")
    print("In the capital, they promise greater adventures and challenges await.")

    while True:
        print("\nWhat will you do?")
        print("1. Accept the invitation and travel to the capital.")
        print("2. Decline the invitation and stay in the town.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nYou accept the invitation and prepare for the journey.")
            print("Excited for new opportunities, you set off with the adventurers to the capital.")
            chapter_four(character)
            break
        elif choice == "2":
            print("\nYou decline the invitation, choosing to stay behind in the town.")
            print("The adventurers respect your decision and wish you well.")
            print("Your adventure ends here. Perhaps the capital will await you another day.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
