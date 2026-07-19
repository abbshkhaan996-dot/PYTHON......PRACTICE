def number_mystery():
    print("🔢 NUMBER MYSTERY")
    print("I'm thinking of a number between 1-100.")
    print("Can you guess it in 7 tries or less?")
    print()

    import random
    secret_number = random.randint(1, 100)
    guesses = 0
    max_guesses = 7
    while guesses < max_guesses:
        print(f"\nGuesses left: {max_guesses - guesses}")
        
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1
            
            if guess == secret_number:
                print(f"🎉 CORRECT! You guessed it in {guesses} tries!")
                break
            elif guess < secret_number:
                print("Too low! Try higher.")
            else:
                print("Too high! Try lower.")
                
        except:
            print("Please enter a number!")
    
    if guesses >= max_guesses:
        print(f"💀 Game over! The number was {secret_number}")

number_mystery()