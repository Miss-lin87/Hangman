import words
import random

def ran_word():
    """used to select a random word from the list of words"""
    x = random.choice(words.word_animal)
    return x

def guess_user():
    """This collects the guess of the user and converts it to lower case"""
    guess = guess_test(input("Please pick a letter "))
    guess = guess.lower()
    return str(guess)

def guess_test(guess):
    """This tests if the input is longer then one or if the input isent a string"""
    try:
        if len(guess) > 1: print("Only pick one letter at a time"); return guess_user()
        else: return str(guess)
    except ValueError: print("Invalid input, only letters are valid"); return guess_user()

def hidden(word=""):
    """This funktion hides the word. Iterates over the word and returns _ in a hidden list"""
    word_lenth = len(word)
    hidden = []
    while word_lenth > 0:
        hidden.append("_")
        word_lenth -= 1
    return hidden

def check_word(word,guess_input,chanses):
    """This funktion checks if the guess is in the hidden word. If it is, return chanses, if not return chanses -1"""
    if guess_input in word: return int(chanses)
    else: chanses -=1; print("the guess in not in the word. " + str(chanses) + " remaining"); return chanses

def check_win(hidden, c_guesses):
    """Function is not used. Was intended to check win state"""
    if "_" in hidden: return hidden, c_guesses
    else: print("You win. You needed " + str(c_guesses) + " guesses"); return True