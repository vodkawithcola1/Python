import random

word_list = ["ardvark", "baboon", "camel"]

#TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess. Checked

#TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

display = []
chosen_word = random.choice(word_list)

for blank in chosen_word:
    display.append("_")

print(f"Psst, the soulution is {chosen_word}")
guess = input("Guess a word: ")
guess.lower()

index = 0

for word in chosen_word:
    if guess in word:
        display[index] = guess
    else:
        display[index] = "_"
    index += 1

print(display)