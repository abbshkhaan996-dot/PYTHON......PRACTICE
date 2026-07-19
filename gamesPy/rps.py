import random

print("Rock Paper Scissors Game")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

# User choice
user = int(input("Enter your choice (1-3): "))

# Computer random choice
computer = random.randint(1, 3)

# Mapping numbers to words
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("You chose:", choices[user])
print("Computer chose:", choices[computer])

# Game logic
if user == computer:
    print("It's a tie!")
elif (user == 1 and computer == 3) or \
     (user == 2 and computer == 1) or \
     (user == 3 and computer == 2):
    print("You win!")
else:
    print("Computer wins!")
