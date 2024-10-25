from words import word_animal
import random
import functions as fun

chanses = int(0)
num_guesses = int(0)
word = []
hidden = []

def game_start():
    """This starts the game, picks global random word, hiddes the word and sets chanses"""
    global word; word = fun.ran_word()
    # print(word)
    global hidden; hidden = fun.hidden(word)
    print("The word has been chosen:\n" + str(hidden))
    global chanses; chanses = len(word) + 2
    print("You now have " + str(chanses) + " chanses to guess the word")

def reveal(word,guess_input):
    """This funktion will reveal the hidden word by replacing the _ spaces with the letter from the word"""
    indexw = [index for index, element in enumerate(word) if element == guess_input]
    for ind in indexw:
        hidden[ind] = word[ind]
    return hidden

def game_run():
    """Just runs the game"""
    game_start()
    global word, chanses, hidden, num_guesses
    while chanses > 0:
            guess = fun.guess_test(fun.guess_user())
            chanses = fun.check_word(word,guess,chanses)
            print(reveal(word,guess))
            num_guesses += 1
            if "_" not in hidden:
                print("You win. You needed " + str(num_guesses) + " guesses to get the word")
                break

game_run()