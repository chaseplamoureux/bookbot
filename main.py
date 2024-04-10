def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    generate_report(book_path, word_count, letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    return len(book.split())


def count_letters(book):
    letter_count = {}
    book = book.lower()
    for letter in book:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


def sort_on(dict):
    return dict["count"]


def generate_report(book_path, word_count, letter_count):
    letters = []
    for k, v in letter_count.items():
        pair = {"char": k, "count": v}
        letters.append(pair)
    letters.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} word found in document")
    print(" ")
    for letter in letters:
        print(f"The '{letter['char']}' was found {letter['count']} times")
    print("--- End report ---")


main()