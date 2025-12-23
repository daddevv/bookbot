def get_word_count(text: str) -> int:
    """Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)


def character_frequency(text: str) -> dict:
    """Calculates the frequency of each character in the given text.

    Args:
        text (str): The text to analyze.
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = {}
    for char in text.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


def sorted_character_frequency(text: str) -> dict:
    """Calculates and returns the character frequency sorted by frequency in descending order.

    Args:
        text (str): The text to analyze.
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values, sorted by frequency.
    """
    freq = character_frequency(text)
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq