import random

# Predefined list of words
words = ["apple", "tiger", "python", "house", "river"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_guesses = 6
incorrect_guesses = 0

print("Welcome to Hangman Game!")

# Create display word
display = ["_"] * len(word)

while incorrect_guesses < max_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check letter in word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1


# Result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)