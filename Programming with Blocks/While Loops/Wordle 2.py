# Christian Lira - Winter 2023
import random

# Define a list of possible words
words = ['synergy', 'leverage', 'ROI', 'scalable', 'disruptive', 'innovative', 'actionable', 'optimization', 'efficiency', 'monetization']

# Choose a random word from the list
secret_word = random.choice(words)

# Initialize the guess counter
guess_count = 0

# Create a list of underscores for each letter in the secret word
hidden_word = ["_" for letter in secret_word]

# Loop until the user guesses the word correctly
while True:
    # Display the hidden word to the user
    print(" ".join(hidden_word))

    # Prompt the user for a guess
    guess = input("Guess the word: ")

    # Increment the guess counter
    guess_count += 1

    # Check if the guess is the same length as the secret word
    if len(guess) != len(secret_word):
        print("Your guess must have the same number of letters as the secret word.")
        continue

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations, you guessed the secret word!")
        break

    # Create a hint for the user based on their guess
    hint = ""
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += "_"

    # Display the hint to the user
    print("Hint: ", hint)

# Display the number of guesses
print("Number of guesses: ", guess_count)
