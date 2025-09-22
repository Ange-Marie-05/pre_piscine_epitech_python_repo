import json
import random

# Charger les mots depuis le JSON
with open("words.json", "r") as f:
    data = json.load(f)
# Charger le best score
with open("best_score.json", "r") as f:
    data2 = json.load(f)

word_list = data["words"]
bestScore = data2["best_score"]

# Fonctions utilitaires
def penalty(count):
    """Retourne le message de pénalité et si le jeu continue."""
    if count == 8:
        return [f"{count} penalties - You lose!", False]
    elif count > 1:
        return [f"{count} penalties", True]
    else:
        return [f"| {count} penalty", True]

def random_word():
    """Tire un mot au hasard depuis la liste."""
    return random.choice(word_list)

def display_word(secret_word, guesses):
    """Affiche le mot avec _ pour les lettres non trouvées."""
    displayed = ""
    correct_count = 0
    for letter in secret_word:
        if letter in guesses:
            displayed += letter.upper() + " "
            correct_count += 1
        else:
            displayed += "_ "
    print(displayed.strip())
    return correct_count

def best_score(word, score_actuel):
    if score_actuel < bestScore:
        with open("best_score.json", "w") as f:
            json.dump({"best_score": score_actuel}, f)
        print(f"Best ever!!! You've guessed {word} in {score_actuel} attempts.")
    else:
        print(f"You've guessed {word} in {score_actuel} attempts. The record is {bestScore} attempts.")


# main code
def hangman():
    secret_word = random_word()
    print(secret_word)

    guesses = []
    penalty_count = 0
    max_penalty = 8

    while penalty_count < max_penalty:
        correct_count = display_word(secret_word, guesses)
        if correct_count == len(secret_word):
            print(f"Correct! The word was: {secret_word.upper()}")
            best_score(secret_word, penalty_count)
            break

        guess = input("Guess a letter: ").strip().lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guesses:
            print("You've already guessed that letter!")
            continue

        guesses.append(guess)

        if guess not in secret_word:
            penalty_count += 1

        retour = penalty(penalty_count)
        print(retour[0])
        if retour[1] == False:
            print(f"💀 Game over! The word was: {secret_word.upper()}")
            best_score(secret_word, penalty_count)
            break

# start game
hangman()

