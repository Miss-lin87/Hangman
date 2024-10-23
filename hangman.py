from words import word_animal
import random
import moduels as mod

chanses = 0

def random_word():
    x = random.choice(word_animal)
    return x

def game():
    word = random_word()
    print(word)
    hidden = mod.hide_word(word)
    print(hidden)
    global chanses; chanses = len(word) + 2
    print(chanses)