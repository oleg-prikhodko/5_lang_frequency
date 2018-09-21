import re
import sys
from collections import Counter


def load_text(filepath):
    with open(filepath) as text_file:
        text = text_file.read()
        return text


def get_ten_most_frequent_words(text, word_count=10):
    text = re.sub(r"\W", " ", text)
    words = text.lower().split()
    frequency_by_word = Counter(words)
    return frequency_by_word.most_common(word_count)


def print_most_frequent_words(most_frequent_words):
    for index, (word, frequency) in enumerate(most_frequent_words, start=1):
        print("{}. {}: {}".format(index, word, frequency))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No filepath argument")

    filepath = sys.argv[1]
    try:
        text = load_text(filepath)
        top_ten_frequent_words = get_ten_most_frequent_words(text)
        print_most_frequent_words(top_ten_frequent_words)
    except FileNotFoundError:
        sys.exit("File not found")
