#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)

print("\n-------> Welcome to Number Guessing Game <-------\n")

def guessing_number():
    """ This Function Guess's The Random Number Between 1 and 100 """
    computer_guess = random.randint(1,100)
    return computer_guess

guess = guessing_number()
print(f"Computer guess is: {guess}")

option_difficulty = input("Enter your choice of difficulty: 'hard' or 'easy'?  ")
if option_difficulty == "hard":
    difficulty = 5
elif option_difficulty == "easy":
    difficulty = 10
else:
    print("Invalid Input! Run Again")

for number in range(1,difficulty + 1):
    player_guess = int(input("Enter your guess : "))

    if(player_guess > guess):
        print("Too High")
    elif(player_guess < guess):
        print("Too Low")
    else:
        print("Your Guess is correct!")
    
    if number >= difficulty:
        print("All your attempts are over!")
