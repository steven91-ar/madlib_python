# Importer la bibliothèque random
import random


# Définir une fonction pour obtenir un mot aléatoire
def get_random_word():
    # Liste de mots
    words = ["incroyable", "énergique", "amusant", "épuisant", "intense", "jouer", "courir", "nager", "Zidane", "Serena Williams", "Mbappé"]
    return random.choice(words)


# Définir une fonction pour jouer au Madlib
def play_madlib():
    # Obtenir les mots aléatoires
    adjective = get_random_word()
    verb = get_random_word()
    famous_person = get_random_word()

    # Créer la phrase Madlib
    madlib = f"Le sport est tellement {adjective}. Cela me rend {adjective} à chaque fois que je joue. " \
         f"J'adore {verb} avec mes amis. Reste motivé(e) et continue à {verb} comme si tu étais {famous_person} !"

    # Afficher la phrase Madlib
    print(madlib)


# Jouer au Madlib
play_madlib()