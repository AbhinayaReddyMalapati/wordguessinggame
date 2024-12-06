import random

# Get the list of words from the user
words = input("Enter a list of words (separated by commas): ").split(',')

# Select a random word from the list
word_to_guess = random.choice(words)

# Initialize guessed letters and tries
guessed_letters = []
tries = 6

while tries > 0:
    # Show the current state of the word
    for letter in word_to_guess:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

    # Ask the player for a letter
    guess = input("Guess a letter: ")

    # Check if the letter is in the word
    if guess in word_to_guess:
        guessed_letters.append(guess)
    else:
        tries -= 1
        print(f"Incorrect! You have {tries} tries left.")

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in word_to_guess):
        print("Good, You've guessed the word.")
        break
else:
    print(f"Fine, you didn't guess the word. It was {word_to_guess}.")

