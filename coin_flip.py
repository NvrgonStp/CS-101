import random


def coin_flip():
    random_chance = random.randint(0, 1)
    if random_chance == 0:
        return "heads"
    elif random_chance == 1:
        return "tails"
    else:
        ValueError("Not a valid option")


print("This is the game of Coin Flip! The game is simple.")
print("Enter a guess of 'heads' or 'tails'. If you're right, you win!")

while True:
    accepted_guesses = ['heads', 'tails']  # Define accepted guesses here
    accepted_retry = ["Y", "N"]
    guess = input("Enter your guess of 'heads' or 'tails': ").strip().lower()

    while guess not in accepted_guesses:
        guess = input(
            "Your guess must be 'heads' or 'tails'. Please try again: ").strip().lower()

    flip = coin_flip()
    if flip == guess:
        outcome = "You won!"
    else:
        outcome = "You lost."
    print(outcome)

    retry = input("Want to try again? Y or N: ").strip().upper()
    while retry not in accepted_retry:
        retry = input(
            "Your response must be 'Y' or 'N'. Please try again: ").strip().upper()
    if retry == "N":
        break
