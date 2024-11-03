import time
from hangman import game_run
from functions import ending as end, countdown

category = "None"
main_text = 1

def word_selection_text():
    print("Please select from the following categories of words.\n"
          "1. Animals\n"
          "2. Car brands\n"
          "3. Cities\n"
          "4. Bodyparts\n"
          "5. Return")
    select = input("Please make a seection: ")
    word_selectin(select)

def word_selectin(select):
    global category
    if select == "1": category = "animals"; end("category"); menu_text()
    elif select == "2": category = "cars"; end("category"); menu_text()
    elif select == "3": category = "cities"; end("category"); menu_text()
    elif select == "4": category = "body"; end("category"); menu_text()
    elif select == "5": print("returning to main menu"); menu_text()
    else: print("Invalid input. Please try again"); 

def menu_text():
    global category, main_text
    if main_text == 1:
        print("Welcome to the game of Hangman. The computer will pick a word at random from the chosen category\n"
          "After this the player will get to pick a letter to quess.\n"
          "If the letter is in the word it will be reveled.\n"
          "The player has a total guesses equal to the number of letters in the word +2")
        time.sleep(2)
        main_text -= 1
    print("Menu:\n"
          "Current category: " + category + "\n"
          "1. Select the category of words\n"
          "2. Start the game\n"
          "3. Exit")
    selection = input("Please select an option: ")
    menu(selection)

def menu(selection):
    global category
    if selection == "1": time.sleep(0.25); word_selection_text() 
    elif selection == "2":
        if category == "None": print("No category has been selected. starting selection menu now"); time.sleep(0.5); word_selection_text()
        else: print("game starting in:"); countdown(5); game_run(category)
    elif selection == "3": time.sleep(0.25); return
    else: print("Invalid input. Please try again"); menu(selection = input(" "))

menu_text()