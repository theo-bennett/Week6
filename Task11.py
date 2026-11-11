import random

def secret_word_game():
    words = [
        "python", "java", "javascript", "csharp",
        "ruby", "swift", "kotlin", "rust", "golang", "php",
        "typescript", "scala", "perl", "haskell", "fortran",
        "variable", "function", "loop", "string", "integer",
        "boolean", "list", "dictionary", "tuple", "exception",
        "compiler", "algorithm", "debug", "keyboard", "program",
        "computer", "software", "hardware", "network", "database",
        "encryption", "decryption", "protocol", "server", "client",
        "framework", "library", "module", "package", "object",
        "class", "inheritance", "polymorphism", "encapsulation", "abstraction",
    ]
    secret_word = random.choice(words)
    revealed = ["_"] * len(secret_word)   

    print("Welcome to the Secret Word Game!")
    print("Guess a single letter or the whole word.")
    print("The secret word has", len(secret_word), "letters.")

    attempts = 10
    while attempts > 0:
        print("\n" + " ".join(revealed))
        guess = input("Enter your guess: ").strip().lower()

        if not guess.isalpha():
            print("Please enter letters only.")
            continue

        if guess == secret_word:
            print("Congratulations! You've guessed the secret word:", secret_word)
            break

        if len(guess) == 1:
            if guess in secret_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        revealed[i] = guess
                print("Yes!", guess, "is in the word.")
                if "_" not in revealed:
                    print("\n" + " ".join(revealed))
                    print("Congratulations! You've revealed the secret word:", secret_word)
                    break
            else:
                attempts -= 1
                print("No", guess, "in the word. You have", attempts, "attempts left.")

        else:
            wrong_place = []
            for i in range(len(guess)):
                letter = guess[i]
                if i < len(secret_word) and letter == secret_word[i]:
                    revealed[i] = letter
                elif letter in secret_word and letter not in wrong_place:
                    wrong_place.append(letter)
            attempts -= 1
            print("Wrong word. You have", attempts, "attempts left.")
            if wrong_place:
                print(", ".join(wrong_place), "is in the word but in a different position.")

    if attempts == 0:
        print("\nSorry, you've run out of attempts. The secret word was:", secret_word)


while True:
    secret_word_game()
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break