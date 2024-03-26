def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def create_list_of_dictionaries(text):
    dict = get_chars_dict(text)
    letters = []
    for index in dict:
        dict_value = {
            'letter': index,
            'num': dict[index]
        }
        letters.append(dict_value)
    letters.sort(key = sort_on, reverse = True)
    return letters

def print_report(text):
    num_words = get_num_words(text)
    num_letters = create_list_of_dictionaries(text)
    print(f"--- Begin  report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for index in num_letters:
        print(f"The {index['letter']} character was found {index['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()