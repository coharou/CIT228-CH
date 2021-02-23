def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words.")

def find_words(filename, search_word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower()
        new_search = search_word.lower()
        num_words = words.count(new_search)
        print(f"The file {filename} has {num_words} words of {new_search}.")

filenames = ['Chapter10/lists.txt', 'Chapter10/dictionaries.txt', 'Chapter10/functions.txt']
for filename in filenames:
    count_words(filename)

user_word = input('What word would you like to search for in the files? Enter here: ')
for filename in filenames:
    find_words(filename, user_word)