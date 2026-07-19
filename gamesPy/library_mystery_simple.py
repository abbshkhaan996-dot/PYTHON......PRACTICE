def library_mystery_simple():
    print("THE LIBRARY BOOK MYSTERY")
    print("A rare book is missing from the library!")

    clue_from_olivia = False
    clue_from_section = False

    while True:
        print("\nWhat do you want to do?")
        print("1. Talk to Emma")
        print("2. Talk to Noah")
        print("3. Talk to Olivia")
        print("4. Check Rare Books Section")
        print("5. Accuse Someone")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Emma: 'I'm just reading. I saw nothing.'")

        elif choice == "2":
            print("Noah: 'I'm working on my computer.'")

        elif choice == "3":
            if not clue_from_olivia:
                print("Olivia: 'I saw someone near the rare books section.'")
                clue_from_olivia = True
            else:
                print("Olivia: 'I already told you what I saw.'")

        elif choice == "4":
            if not clue_from_section:
                print("You find Noah's library card!")
                clue_from_section = True
            else:
                print("You already checked here.")

        elif choice == "5":
            print("\nWho do you accuse?")
            print("1. Emma")
            print("2. Noah")
            print("3. Olivia")

            acc = input("Your choice: ")

            if acc == "2":
                if clue_from_olivia and clue_from_section:
                    print("Noah admits he borrowed the book!")
                    print("Mystery solved!")
                else:
                    print("You don't have enough clues to accuse Noah.")
                break
            else:
                print("Wrong accusation! Game over.")
                break

        elif choice == "6":
            print("You gave up. Mystery unsolved.")
            break

        else:
            print("Please enter a valid number.")
