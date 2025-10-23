def get_books_text():
    path_to_file = ("books/frankenstein.txt")
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_books_text()
    print(book_text)

main()