from chapter_eleven import chapter_eleven

def chapter_ten(character):
    """Chapter 10: Inside the Island Ruin"""
    print("\n--- Chapter 10: Inside the Island Ruin ---")
    print("You step into the dark and ancient ruin. The walls are adorned with faded carvings, and the air is cold.")
    print("As you move deeper into the ruin, you reach a fork with three paths.")
    print("The paths lead left, center, and right. One of them leads to the artifact, while the others hold traps.")

    while True:
        print("\nWhich path will you choose?")
        print("1. Left path.")
        print("2. Center path.")
        print("3. Right path.")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1" or choice == "3":
            print("\n--- Trap Encountered! ---")
            print("You take the wrong path and trigger a trap! Arrows shoot from the walls, and you barely escape.")
            print("You loop back to the fork, realizing your mistake.")
        elif choice == "2":
            print("\n--- Correct Path ---")
            print("You follow the center path, and the air grows warmer as you approach a large chamber.")
            artifact_chamber(character)
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def artifact_chamber(character):
    """Artifact Chamber"""
    print("\n--- Artifact Chamber ---")
    print("You enter a vast chamber illuminated by glowing crystals.")
    print("In the center of the room, on a pedestal, lies the powerful artifact you’ve been seeking.")
    print(f"{character['name']} approaches carefully, sensing the immense power emanating from it.")
    print("You retrieve the artifact, feeling its energy coursing through you.")
    character['artifact'] = "Ancient Artifact of Power"
    print(f"You now possess the {character['artifact']}.")

    print("\nHowever, before you can leave, a sinister voice echoes through the chamber.")
    print("'Well, well, it seems someone has beaten me to it,' a figure says as they step out of the shadows.")
    print("A sorcerer appears, their eyes glowing with dark magic. 'Hand over the artifact, and I might spare you.'")

    print("\nWith no intention of giving up the artifact, you prepare for a battle.")
    chapter_eleven(character)
