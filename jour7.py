# hangman game
import random
from english_words import get_english_words_set

# first brick | modified
def penalty(param, x = 0):
    if x >= 8:
        return [f"{param} penalties - You loose!", False]
    elif x > 1:
        return [f"{param} penalties", True]
    else:
        return [f"| {param} penalty", True]

# next brick
def return_random_number():
    return random.randrange(1, 7)

# fisrt package | modified
def random_word():
    english_word = get_english_words_set(['web2'], lower = False)
    for x in english_word:
        y = x
        break
    return y

# another brick(in the wall) | modified
def underscore_space(param, guess, penalty_number, win = 1):
    for x in param:
        if x in guess:
            print(x.upper(), end=" ")
            win += 1
        else:
            print("_", end=" ")

    x = penalty(penalty_number, penalty_number)
    print(x[0])
    return [win, penalty_number, x]

# pseudocode - pfff

# implementation
guess_word = random_word()
print(guess_word)
penalty_count = 0
guess = [""]
x = [0, 0, []]

while penalty_count <= 8:
    if x[0] != len(guess_word):
        x = underscore_space(guess_word, guess, penalty_count)
        if x[2][1] == True:
            guess.append(*(input("> ")).strip("> ").split())
        else:
            break
        if guess[-1] not in guess_word:
            penalty_count += 1
    else:
        print(f"{guess_word}: correct guess")
        break

# je vais m'en arreter là, sinon je vais devenir fou xD

