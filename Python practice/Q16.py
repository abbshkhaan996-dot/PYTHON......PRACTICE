import random
secret = random.randint(1, 10)
guess = int(input("Guess: "))
if guess == secret:
    print("Correct!")
else:
    print("Wrong! Number was", secret)
