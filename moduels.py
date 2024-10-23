import random
import hangman

def guess_user():
    guess = guess_test(input("Please pick a letter "))
    return str(guess)

def guess_test(guess):
    try:
        if len(guess) > 1: print("Only pick one letter at a time"); return guess_user()
        else: return str(guess)
    except ValueError: print("Invalid input, only letters are valid"); return guess_user()

def hide_word(word=""):
    word_lenth = len(word)
    hidden = []
    while word_lenth > 0:
        hidden.append("_")
        word_lenth -= 1
    return hidden

def reveal(words, guess_input):
    if guess_input in words:
        k = words.count(guess_input)

def check_word(word, guess_input, chanses):
    if guess_input in word: return guess_input
    else: chanses -= 1; print("the guess in not in the word. " + str(chanses) + " remaining"), chanses

def plug_word(hidden, word, guess_input):
    x = list(word)
    # for x in range(len(x)):
        # if guess_input == word: word
    return x