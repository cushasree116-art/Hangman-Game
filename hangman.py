import random
words = ["python", "apple", "coding", "laptop", "school"]
word = random.choice(words)
guessed_letters = []
chances = 6
print("🎮 Welcome to Hangman Game")
while chances > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").lower()
    if guess in word:
        print("✅ Correct Guess!")
        guessed_letters.append(guess)
    else:
        chances -= 1
        print("❌ Wrong Guess!")
        print("Remaining chances:", chances)# Hangman Game

This is a simple Hangman Game developed using Python.

## Features
- Random word selection
- User guesses letters
- Limited attempts
- Win/Lose conditions

## Developed For
CodeAlpha Internship
if chances == 0:
    print("\n😢 Game Over!")
    print("The word was:", word)