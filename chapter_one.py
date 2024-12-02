from chapter_two import chapter_two

def chapter_one(character):
    """Chapter 1: Arrival in Town"""
    print("\n--- Chapter 1: Arrival in Town ---")
    print(f"{character['name']} arrives in a bustling town, seeking adventure.")
    print("While exploring, you meet a group of seasoned adventurers.")
    print("They approach you with an offer: 'We need your help on a dangerous quest.'")

    while True:
        print("\nWhat will you do?")
        print("1. Accept the quest.")
        print("2. Decline the quest.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nYou decide to help the adventurers. Together, you prepare for the quest and head to the nearby mines.")
            chapter_two(character)
            break
        elif choice == "2":
            print("\nYou decline the quest. The adventurers look disappointed and walk away.")
            print("Your adventure ends here. Perhaps next time you'll take the chance.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
