import random

def choose_word():
    # List of words for the game
    words = ["PYTHON", "JAVA", "JAVASCRIPT", "RUBY", "CPLUSPLUS", "HTML"]

    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word().upper()  # Choose a random word and convert to uppercase
    guessed_letters = []  # List to store guessed letters
    attempts = 6  # Number of attempts allowed

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", " ".join(guessed_letters))
        print("Word:", display_word(secret_word, guessed_letters))

        guess = input("Enter a letter or the full word guess: ").upper()

        if len(guess) == 1:  # Guessing a letter
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts -= 1
        elif len(guess) == len(secret_word) and guess.isalpha():  # Guessing the whole word
            if guess == secret_word:
                print("Congratulations! You guessed the word!")
                return
            else:
                print("Incorrect guess.")
                attempts -= 1
        else:
            print("Invalid input. Please enter a valid letter or the full word guess.")

        # Check if the word has been guessed
        if "_" not in display_word(secret_word, guessed_letters):
            print("Congratulations! You guessed the word:", secret_word)
            return

    print("You ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
