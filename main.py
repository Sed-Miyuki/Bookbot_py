from stats import no_of_words,count_characters
import sys
def get_book_text(path):
    file_contents=""
    with open(path) as f:
        file_contents=f.read()
    return file_contents

def sort_on(dict_item):
    return dict_item["num"]

def main():
    if(len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path=sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    tex=get_book_text(path)
    num_words=no_of_words(tex)
    freq=count_characters(tex)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_list = []
    for char in freq:
        char_list.append({"char": char, "num": freq[char]})
    char_list.sort(key=sort_on, reverse=True)    
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
