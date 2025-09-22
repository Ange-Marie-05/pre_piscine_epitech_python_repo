import nltk
# télécharger le corpus la première fois
nltk.download('words')

import json
import random
from nltk.corpus import words


# Listes des mots anglais valides, 2 à 3 lettres
words_list = [w.lower() for w in words.words() if w.isalpha() and (len(w) in range(3, 11))]

# Mélanger et prendre jusqu'à 100 000 mots
random.shuffle(words_list)
words_list = words_list[:100000]
words_list.sort()

# Sauvegarder dans words.json
with open("words.json", "w") as f:
    json.dump({"words": words_list}, f, indent='\t')

print("✅ Fichier words.json généré avec", len(words_list), "mots.")