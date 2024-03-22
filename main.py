def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    sorted_letter_count = get_sorted_letter_count(letter_count)

    print()
    print(f"----Begin Report of Document:{book_path}----")
    print()
    print(f"Found {word_count} words in the document")
    print()
    print(f"Here is a breakdown of the letters used in the document:")
    print()
    
    for letter in sorted_letter_count:
        if not letter['letter'].isalpha():
            continue
        print(f"Letter '{letter['letter']}' appears: {letter['num']} times")

    print()
    print(f"----End of Report on Document:{book_path}----")
    print()

def sort_on(dict):
    return dict["num"]

def get_sorted_letter_count(dict):
    sorted_letters = []
    for i in dict:
        sorted_letters.append({"letter": i, "num": dict[i]})
        sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters
  

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = {}
    for i in text:
        lower_letter = i.lower()
        if lower_letter in letters:
            letters[lower_letter] += 1
        else:
            letters[lower_letter] = 1
    return letters
        


def get_book_text(text):
    with open(text) as f:
        return f.read()



main()