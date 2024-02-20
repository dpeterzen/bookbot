def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = len(text.split())
    return words


main()