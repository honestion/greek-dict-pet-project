from dictionary import greek_words
from start_menu import start_menu

'''Delete word from dictionary fuction'''
def delete_word():
    word = input("What word you want to delete? ")
    for i in range(len(greek_words)):
        if greek_words[i]["word"] == word: 
            greek_words.pop(i)
            break

    start_menu()