import sys
from stats import get_num_words, count_letters, sorted_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    letter_count = count_letters(text)
    sorted_characters = sorted_dict(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for char in sorted_characters:
        if char.isalpha():
            print(f"{char}: {sorted_characters[char]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as path:
        files_contents = path.read()
        return files_contents

if __name__ == '__main__':
    main()