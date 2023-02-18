# Store the secret word
secret_word = "apple"

# Initialize the guess counter
guess_count = 0

# Loop until the user guesses the correct word
while True:
    # Prompt the user for a guess
    guess = input("Guess the secret word: ")

    # Increment the guess counter
    guess_count += 1

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations, you guessed the secret word!")
        break

# Display the number of guesses
print("Number of guesses: ", guess_count)