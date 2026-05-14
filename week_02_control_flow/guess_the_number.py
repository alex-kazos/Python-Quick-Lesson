import random


MAX_ATTEMPTS = 5


print("Guess the Number")
print("I am thinking of a number from 1 to 20.")

secret_number = random.randint(1, 20)
guesses = []

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess_text = input(f"Attempt {attempt}/{MAX_ATTEMPTS}: ")

    if not guess_text.isdigit():
        print("Please type a whole number.")
        continue

    guess = int(guess_text)
    guesses.append(guess)

    if guess == secret_number:
        print("You got it!")
        break
    if guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Out of attempts. The number was {secret_number}.")

print(f"Your guesses: {guesses}")

