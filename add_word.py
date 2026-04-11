from dictionary import greek_words
from start_menu import start_menu
'''Function to add word to dictionary'''
def add_word(): 
    # get info about adding word
    word = input("What's word? ")    
    trancription = input("What's its trancription? ")
    translation = input("What's its translation? ")
    category = input("Where is this word from? ")
    # create new dict to add it in a general list of dictionaries
    new_word = {
        "word": word,
        "transcription": trancription,
        "translation": translation,
        "category": category
    }
    # add new word in general list and  and quit to menu
    greek_words.append(new_word)
    start_menu()