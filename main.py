def main():
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
        num_words = words(file_contents)
        letter_dict = letters(file_contents)
        sorted_letter_list = sort_letter(letter_dict)
        create_report(num_words, sorted_letter_list)


def words(book):
    return len(book.split())


def letters(book):
    char_dict = {}
    for char in book.lower():
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_letter(dict):
    letter_list = []
    for letter in dict:
        letter_list.append({"letter": letter, "num": dict[letter]})
    letter_list.sort(reverse = True, key = sort_on)
    return letter_list

def create_report(num_words, sorted_letter_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for sorted_letter in sorted_letter_list:
        print(f"The '{sorted_letter["letter"]}' character was found {sorted_letter["num"]} times")
    print("--- End report ---")

main()