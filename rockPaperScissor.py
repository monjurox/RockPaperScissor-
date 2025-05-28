import random

print("~"*57)
print("Welcome to Rock, Paper, Scissors!".center(60))
print("~"*57)

# computer choices
choices = ["rock", "paper", "scissors"]
guess = random.choice(choices)

# user input
while True:
    user_input = input(
        "Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()

    if user_input == "exit":
        print("Thanks for playing!")
        break

    if user_input not in choices:
        print("Invalid choice. Please try again.")
        continue

    print(f"You chose: {user_input}")
    print(f"Computer chose: {guess}")

    if user_input == guess:
        print("It's a tie!")
    elif (user_input == "rock" and guess == "scissors") or \
         (user_input == "paper" and guess == "rock") or \
         (user_input == "scissors" and guess == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Reset computer choice for the next round
    guess = random.choice(choices)
