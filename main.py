import sys

from stats import get_word_count, character_frequency, sorted_character_frequency

def get_book_text(filepath) -> str:
    """Reads the text of a book from a given file path.

    Args:
        filepath (str): The path to the text file containing the book.
    Returns:
        str: The content of the book as a string.
    """

    with open(filepath, 'r', encoding='utf-8') as file:
        book_text = file.read()
    return book_text



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_char_freq = sorted_character_frequency(book_text)
    for char, freq in sorted_char_freq.items():
        if char.isalpha():
            print(f"{char}: {freq}")

if __name__ == "__main__":
    main()