def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    static_chars = get_static_characters(text)
    report = get_statict_chars_report(static_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print(report)
    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()

def get_num_words(string):
    return len(string.split())

def get_static_characters(string):
    char_dict = {}

    for char in string:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(item):
    return item[1]

def get_statict_chars_report(char_dict):
    report = ""
    alphabet_list = []

    for item in char_dict.items():
        if not item[0].isalpha():
            continue
        alphabet_list.append(item)

    alphabet_list.sort(reverse=True, key=sort_on)

    for item in alphabet_list:
        report += f"The '{item[0]}' character was found {item[1]} times\n"

    report = report[:-1]

    return report

if __name__ == "__main__":
    main()
