# ====
# NUMBER GAME
# ====
# Similar to a previous project I did with JavaScript, this will be a game where the
# program generates a pseudo-random integer and the user has 3 attempts to correctly
# input a number that matches.

# Importing "random" from the numpy library.
from numpy import random

# Establishing the number of attempts
attempts = 3

# Creating a function containing the game
def numberGame(guess):
    # Stating attempts as a global variable to clarify it as not being a new local variable
    global attempts
    # Creating a random number
    randomNumber = random.randint(10)

    # A print line for testing purposes
    print(f"The number to guess is: {randomNumber}")
    # A while loop: while the user has more than 0 attempts, they can keep guessing
    while(attempts > 0):
        # If their guess is more than the random number
        if(guess > randomNumber):
            guess = int(input("Too high! Try again: "))
            # Decreasing the number of attempts
            attempts -= 1
            print(f"Number of attempts left: {attempts}")
        # If their guess is lower than the random number
        elif(guess < randomNumber):
            guess = int(input("Too low! Try again: "))
            attempts -= 1
            print(f"Number of attempts left: {attempts}")
        # Else, the last possible outcome is that they guessed it correctly
        else:
            print(f"You win! You correctly guessed: {randomNumber}")
            # Must insert a break or the if statement will continue to fulfill this
            # conditional statement and repeat continuously
            break
    else:
        # Once the user has 0 attempts, they get a game over
        print("No more retries. GAME OVER.")

print("====")
print("Welcome to the Number Guessing Game!")
print("====")

# Ask the user to input a number, making sure its value is valid and according to the rules
while True:
    # Use a try-except block to catch input errors
    try:
        guess = int(input("Please input a number between 1 and 10: "))
        if(1 <= guess <= 10):
            # If the number meets the criteria, break the loop
            break
        else:
            print("This number is not allowed. Please try another number between 1 and 10.")
    except ValueError:
        print("This input is invalid. Please try again.")

numberGame(guess)