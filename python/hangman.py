import random

# List of words
words = ['python', 'hangman', 'programming', 'code', 'game', 'developer', 'keyboard']

# Choose a random word from the list
chosen_word = random.choice(words)
word_length = len(chosen_word)

# Create a list with underscores for hidden letters
display = ['_'] * word_length

# Maximum number of tries
lives = 6

# Store guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Try to guess the word, one letter at a time.")
print("You have", lives, "lives.")
print(' '.join(display))

# Game loop
while lives > 0 and '_' in display:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("❗You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct guess!")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print("❌ Wrong guess! Lives left:", lives)

    print(' '.join(display))

# Final result
if '_' not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
