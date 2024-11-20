import random

# List of superhero movies
superhero_movies = [
    "avengers endgame", 
    "the dark knight", 
    "iron man", 
    "spider man no way home",
    "black panther",
    "wonder woman",
    "doctor strange",
    "guardians of the galaxy",
    "batman vs superman",
    "thor ragnarok"
]

def display_word(secret_word, guessed_letters):
    """
    Display the current state of the secret word with underscores for unguessed letters.
    """
    return ' '.join([char if char in guessed_letters or char == ' ' else '_' for char in secret_word])

def hangman():
    print("Welcome to Hangman: Superhero Movies Edition!")
    secret_word = random.choice(superhero_movies).lower()
    guessed_letters = set()
    attempts_left = 7

    print(f"\nGuess the superhero movie! You have {attempts_left} attempts.")
    print(display_word(secret_word, guessed_letters))

    while attempts_left > 0:
        guess = input("\nEnter a letter or guess the entire movie: ").lower()

        if len(guess) == 1:
            # Single letter guess
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try again!")
            elif guess in secret_word:
                guessed_letters.add(guess)
                print(f"Good job! '{guess}' is in the movie title.")
            else:
                guessed_letters.add(guess)
                attempts_left -= 1
                print(f"Oops! '{guess}' is not in the movie title. Attempts left: {attempts_left}")
        else:
            # Full word guess
            if guess == secret_word:
                print(f"Congratulations! You guessed the movie: '{secret_word}'")
                break
            else:
                attempts_left -= 1
                print(f"Wrong guess! Attempts left: {attempts_left}")

        # Show the current state of the word
        current_display = display_word(secret_word, guessed_letters)
        print("\n" + current_display)

        # Check if the player has guessed all letters
        if '_' not in current_display:
            print(f"Congratulations! You guessed the movie: '{secret_word}'")
            break

    if attempts_left == 0:
        print(f"\nGame Over! The movie was: '{secret_word}'")

# Run the Hangman game
if __name__ == "__main__":
    hangman()