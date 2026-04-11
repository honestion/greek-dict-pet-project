from dictionary import greek_words

'''Fuction to show all words in dictionary'''
def show_words():
    for item in greek_words:
        print(item["word"])