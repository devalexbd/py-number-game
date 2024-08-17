# Making my number game code more efficient

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

    while(attempts > 1):
        # If the guess is correct...
        if(guess > randomNumber):
            print("Too high! Try again: ")
            attempts -= 1
            print(f"Number of attempts left: {attempts}")
        elif(guess < randomNumber):
            print("Too low! Try again: ")
            attempts -= 1
            print(f"Number of attempts left: {attempts}")
        else:
            print(f"You win! You correctly guessed: {randomNumber}")
            break

        # Using try-except to catch incorrect answers
        try:
            guess = int(input("Please enter your new guess: "))
        except ValueError:
            print("Your input is invalid. Please enter a number.")
            continue

        # Catching the user entering numbers outside the state parameters
        while guess < 1 or guess > 10:
            try:
                guess = int(input("This number is not allowed. Please try another: "))
            except ValueError:
                print("Your input is invalid. Please enter a number.")

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