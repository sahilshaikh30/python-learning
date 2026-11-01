import random

# ---------------- SNAKE-WATER-GUN GAME ----------------

while True:

    # Computer randomly selects a new choice for every round
    c = random.choice([1, -1, 0])

    # Ask the user to enter their choice
    h = input("Enter your choice (s,w,g): ")

    # Convert user choice into numerical values
    choices = {"s": 1, "w": -1, "g": 0}
    y = choices[h]

    # Convert numerical values back into choice names
    reverse_dict = {1: "s", -1: "w", 0: "g"}

    # Display both choices
    print(f"You choose: {reverse_dict[y]} and Computer choose: {reverse_dict[c]}")

    # ---------------- CHECK GAME RESULT ----------------

    if c == y:
        print("It's a draw")

    else:
        if c == 1 and y == -1:
            print("You lose")
        elif c == 1 and y == 0:
            print("You win")
        elif c == -1 and y == 1:
            print("You win")
        elif c == -1 and y == 0:
            print("You lose")
        elif c == 0 and y == 1:
            print("You lose")
        elif c == 0 and y == -1:
            print("You win")

    # ---------------- PLAY AGAIN ----------------

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() == "no":
        print("Thanks for playing!")
        break

    print("\nStarting a new round...\n")