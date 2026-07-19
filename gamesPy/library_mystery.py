def library_mystery():
    print("THE LIBRARY BOOK MYSTERY")
    print("A rare book is missing from the library!")
    print("Find it before the librarian notices!")

    global clues, talked_to_olivia, found_card_clue
    clues = 0
    talked_to_olivia = False
    found_card_clue = False

    while True:
        print("\nWhat do you want to do?")
        print("1. Talk to Emma")
        print("2. Talk to Noah")
        print("3. Talk to Olivia")
        print("4. Check Rare Books Section")
        print("5. Make accusation")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            talk_to_emma()
        elif choice == "2":
            talk_to_noah()
        elif choice == "3":
            talk_to_olivia()
        elif choice == "4":
            check_rare_books_section()
        elif choice == "5":
            finished = make_accusation()
            if finished:
                break  # Game ends after accusation
        elif choice == "6":
            print("You gave up. Mystery remains unsolved.")
            break
        else:
            print("Please enter a valid choice (1-6).")


def keys_riddle():
    print("RIDDLE: What has keys but can't open locks?")
    ans = input("Your answer: ").strip().lower()
    return ans == "keyboard"

def shadow_riddle():
    print("RIDDLE: Who is always present but is never seen?")
    ans = input("Your answer: ").strip().lower()
    return ans in ["shadow", "silence"]

def talk_to_emma():
    print("You talk to Emma.")
    print("Emma: 'I'm always reading, but I haven't seen anything suspicious.'")

def talk_to_noah():
    print("You talk to Noah.")
    print("Noah: 'I’m busy with my computer work. I don’t know anything about the missing book.'")

def talk_to_olivia():
    global clues, talked_to_olivia
    if not talked_to_olivia:
        if shadow_riddle():
            print("Olivia: 'I saw someone near the rare books section...'")
            talked_to_olivia = True
            clues += 1
        else:
            print("Olivia doesn't trust you until you answer her riddle.")
    else:
        print("Olivia has already given you a clue.")

def check_rare_books_section():
    global clues, found_card_clue
    print("\nYou check the RARE BOOKS SECTION...")
    print("You find a library card dropped on the floor!")
    check = input("Check whose card it is? (y/n): ").strip().lower()
    if check == "y":
        if keys_riddle():
            print("It belongs to Noah!")
            found_card_clue = True
            clues += 1
        else:
            print("You failed to solve the riddle. No clue gained.")
    else:
        print("You put the card back.")

def confront_noah():
    print("\nYou confront Noah...")
    print("Noah: 'Okay, I borrowed the book to scan it.'")
    print("'I wanted a digital copy for my research.'")
    print("He returns the book and apologizes.")
    print("MYSTERY SOLVED! The book is safe.")

def make_accusation():
    global clues
    print("\nWho do you accuse?")
    print("1. Emma")
    print("2. Noah")
    print("3. Olivia")
    print("4. Go back")
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        print("Emma: 'I’m innocent! I was just reading all along.'")
        print("Wrong accusation! You lost the game.")
        return True  # Game ends
    elif choice == "2":
        if clues >= 2:
            confront_noah()
            return True  # Game ends, player wins
        else:
            print("You don't have enough clues to accuse Noah confidently.")
            return False
    elif choice == "3":
        print("Olivia: 'I didn’t do it! Why would I steal a book?'")
        print("Wrong accusation! You lost the game.")
        return True  # Game ends
    else:
        print("You decided not to accuse anyone yet.")
        return False
    
    print(f"\nClues found: {clues}/2")
    print("-" * 30)