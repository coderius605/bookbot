def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)

    report = count_characters(file_contents)

    converted_report = convert_to_list(report)

    converted_report.sort(reverse=True, key=sort_on)

    generate_report(converted_report, file_contents)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)


def count_characters(string):
    lowered_string = string.lower()
    words = lowered_string.split()
    char_counts = {}

    for word in words:
        for character in word:
            if not character.isalpha():
                continue
            elif character in char_counts:
                char_counts[character] = char_counts[character] + 1
            else:
                char_counts[character] = 1
    
    return char_counts


def convert_to_list(dictionary):
    list = []

    for item in dictionary:
        key_value_pair = {'char': item, 'num': dictionary[item]}
        list.append(key_value_pair)
    
    return list

def sort_on(dict):
    return dict["num"]

def generate_report(list, string):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(string)} words found in the document")

    for letter_stats in list:
        print(f"The '{letter_stats['char']}' character was found {letter_stats['num']} times")

main()