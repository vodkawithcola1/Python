import random
import hangman_art
import hangman_words


#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and
# 'display' has no more blanks ("_"). Then you can tell the user they've won.


display = []
chosen_word = random.choice(hangman_words.word_list)
isPlaying = True
lives = 6
hangman_index = 6

print(hangman_art.logo)

for blank in chosen_word:
    display.append("_")

while isPlaying:
    index = 0

    guess = input("Guess a word: ").lower()

    if guess in display:
        print("You've already guessed that word!")

    for word in chosen_word:
        if guess in word:
            display[index] = guess
        index += 1

    if guess not in chosen_word:
        lives -= 1
        print(f"".join(hangman_art.stages[hangman_index]))
        hangman_index -= 1

    print(f"".join(display))
    if "_" not in display:
        isPlaying = False
        print("You won!")

    if lives == -1:
        isPlaying = False
        print("You lost!")
        print(f"The word was {chosen_word}")
