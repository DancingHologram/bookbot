def sort_on(items):
    return items["num"]
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
def character_count():
   character_counts = {}
   book_words = get_books()
   char_occurence = book_words.lower()
   for c in char_occurence:
        if c.isalpha():
            if c not in character_counts:
                character_counts[c] = 1
            else:
                character_counts[c] += 1
   return character_counts
def sorted_list():
    unsorted_list = []
    unsorted_dict = character_count()
    for ch, cnt in unsorted_dict.items():
        unsorted_list.append({"char":ch, "num": cnt})
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list