def sort_on(items):
    return items["num"]
def get_books(path):
    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents
def word_count(path):
    book_words = get_books(path)
    book_word_count = book_words.split()
    total_words = len(book_word_count)
    return total_words
def character_count(path):
   character_counts = {}
   book_words = get_books(path)
   char_occurence = book_words.lower()
   for c in char_occurence:
        if c.isalpha():
            if c not in character_counts:
                character_counts[c] = 1
            else:
                character_counts[c] += 1
   return character_counts
def sorted_list(path):
    unsorted_list = []
    unsorted_dict = character_count(path)
    for ch, cnt in unsorted_dict.items():
        unsorted_list.append({"char":ch, "num": cnt})
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list