from stats import word_count, sorted_list

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count()} total words")
    print("--------- Character Count -------")
    for item in sorted_list():
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

main()