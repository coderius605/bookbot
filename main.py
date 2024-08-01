def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    print(count_words(file_contents))

    print(count_characters(file_contents))


def count_words(string):
    words = string.split()
    return len(words)


def count_characters(string):
    lowered_string = string.lower()
    words = lowered_string.split()
    char_counts = {}

    for word in words:
        for character in word:
            if character in char_counts:
                char_counts[character] = char_counts[character] + 1
            else:
                char_counts[character] = 1
    
    return char_counts



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()