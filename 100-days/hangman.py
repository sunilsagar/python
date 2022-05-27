word_list = ["ardvark", "baboon", "camel"]

import random

chosen_word = random.choice(word_list)

print(chosen_word)

display = []
#for letter in chosen_word:
#    display += "_"
#print(display)

#alternative way
for _ in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

#for letter in chosen_word:
#    if letter == guess:
#         print("Right")
#    else:
#        print("Wrong")

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)

