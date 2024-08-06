import random

words = ['apple','banana','chocolate','dream','elephant','function','grapes','happy','incubation','jelly','kangaroo','library','mango','north','ostrich','party','question','rain','strong','trouble','unique','ventilation','wonder','xerotic','yummy','zebra','aptitude','biryani','challenge','domestic','eligent','fascinate','growing','horse','ice cream','journey','kettle','lion','monkey','number','occasion','priority','queen','railway','straight','train','universe','village','wanted','xerox','yellow','zigzag']

word_to_guess = random.choice(words)

hint_letter = random.choice(word_to_guess)

guessed_letters = [hint_letter]
tries = 6

print(f"Hint: The word contains the letter '{hint_letter}'")

while tries > 0:
    
    for letter in word_to_guess:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()
    guess = input("Guess a letter: ")

    if guess in word_to_guess:
        guessed_letters.append(guess)
    else:
        tries -= 1
        print(f"Incorrect! You have {tries} tries left.")

    if all(letter in guessed_letters for letter in word_to_guess):
        print("the word is : ",word_to_guess)
        print("Congratulations! You've guessed the word.")
        
        break
else:
    print(f"Sorry, you didn't guess the word. It was {word_to_guess}.")


