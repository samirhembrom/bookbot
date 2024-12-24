def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    get_report(sort_character(create_list(get_character_count(text))),book_path,get_word_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    text=text.lower()
    freq = {}
    for char in text:
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def create_list(freq):
    chars = []
    for key in freq.keys():
        chars.append({"char":key,"count":freq[key]})
    return chars

def sort_on(dict):
    return dict["count"]

def sort_character(chars):
    chars.sort(reverse=True,key=sort_on)
    return chars

def get_report(chars,path,words):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for d in chars:
        if d["char"].isalpha():
            print(f"The '{d["char"]}' character was found {d["count"]} times")
    print(f"--- End of report ---")

if __name__ == '__main__':
    main()
