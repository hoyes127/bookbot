
def book_word_count(book):
    word_list = book.split()
    return word_list

def book_letter_count(book):
    word_list = book_word_count(book)
    letter_count = {}
    for word in word_list:
        for letter in word:
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sort_on(letter):
    return letter["num"]


def sort_letter_count(letter_count):
    letter_list = []
    for letter in letter_count:
        letter_list.append({"char": letter, "num": letter_count[letter]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list