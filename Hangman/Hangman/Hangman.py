import random

word_list = ["ardvark", "baboon", "camel"]

#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and
# 'display' has no more blanks ("_"). Then you can tell the user they've won.

display = []
chosen_word = random.choice(word_list)
isPlaying = True

print(f"Psst, the soulution is {chosen_word}")

for blank in chosen_word:
    display.append("_")

while isPlaying:
    index = 0
    guess = input("Guess a word: ").lower()

    for word in chosen_word:
        if guess in word:
            display[index] = guess
        index += 1
    print(display)

    if "_" not in display:
        isPlaying = False
        print("You won!")

