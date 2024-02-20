def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_dict = count_letters(text)

    sorted_letters = sort_letter_dict(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for dict in sorted_letters:
        print(f"The {dict['letter']} character was found {dict['num']} times")
    
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = len(text.split())
    return words

def count_letters(text):
    letter_dict = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in letter_dict:
            letter_dict[c] += 1
        else:
            letter_dict[c] = 1
    
    return letter_dict

def sort_on(dict):
    return dict["num"]

def sort_letter_dict(dict):
    letter_list = []

    for letter in dict:
        temp_dict = {}
        if letter.isalpha():
            temp_dict["letter"] = letter
            temp_dict["num"] = dict[letter]
            letter_list.append(temp_dict)
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

main()