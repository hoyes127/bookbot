from stats import book_word_count, book_letter_count, sort_letter_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    word_count = book_word_count(book)
    letter_count = book_letter_count(book)
    sorted_letters = sort_letter_count(letter_count)
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}\n"
        "----------- Word Count ----------\n"
        f"Found {len(word_count)} total words\n"
        "--------- Character Count -------\n"
    )
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")


main()

