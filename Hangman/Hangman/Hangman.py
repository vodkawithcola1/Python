import random

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. CHECKED

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. CHECKED

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. CHECKED

chosen_word = random.choice(word_list)

guess = input("Guess a word: ")
guess.lower()

for word in chosen_word:
    if guess in word:
        print("Correct")
    else:
        print("Wrong")