
# Import randint to generate a random integer
from random import randint

# Generate a secret number between 1 and 100
secret_number = randint(1, 100)

# Initialize guess and attempt counter
guess = 0
attempt = 0


# ---------------- NUMBER GUESSING GAME ----------------

# Continue the game until the user guesses the correct number
while guess != secret_number:

    # Ask the user to enter a number
    guess = int(input("Guess the number: "))

    # If the guess is greater than the secret number
    if (guess > secret_number):
        print("Lower number please")

        # Increase attempt count for an incorrect guess
        attempt += 1

    # If the guess is smaller than the secret number
    elif (guess < secret_number):
        print("Higher number please")

        # Increase attempt count for an incorrect guess
        attempt += 1

    # If neither condition is true, the guess is correct
    else:
        print(f"You guessed it in attempts: {attempt}")
        