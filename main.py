from start_menu import start_menu
from add_word import add_word
from delete_word import delete_word
from show_words import show_words

def main():
    while True:
        start_menu()
        action = int(input()) # action request to get what to do
        # checking key actions
        match action:
            case 1:
                show_words()
            case 2:
                add_word()
            case 3:
                delete_word()
            case 4:
                return False
            case _:
                print('Type num from 1 to 4, nothing else')

main()