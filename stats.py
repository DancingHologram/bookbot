def get_books():
    path_to_file = ("books/frankenstein.txt")
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def word_count():
    book_words = get_books()
    book_word_count = book_words.split()
    total_words = len(book_word_count)
    return total_words
