import random

def select_word():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)

def start_hangman():
    word = select_word()
    guessed_letters = set()
    total_attempts = 5

    for attempt in range(total_attempts):
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guesse that leter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            print("Incorrec guess. You have", total_attempts - attempt - 1, "attempts left.")

        if display_word == word:
            print("Congratulations! You won!")
            break

    if display_word != word:
        print("Sorry, you ran out of attempts. The word was:", word)
        
print(start_hangman())
