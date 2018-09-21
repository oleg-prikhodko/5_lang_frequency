import re
import sys
from collections import defaultdict


def load_text(filepath):
    with open(filepath) as text_file:
        text = text_file.read()
        return text


def get_ten_most_frequent_words(text):
    text = re.sub(r"\W", " ", text)
    words = text.lower().split()
    frequency_by_word = defaultdict(lambda: 0)
    for word in words:
        frequency_by_word[word] += 1

    top_ten_frequent_words = sorted(
        frequency_by_word.items(), key=lambda item: item[1], reverse=True
    )[:10]
    return top_ten_frequent_words


def print_most_frequent_words(most_frequent_words):
    for index, (word, frequency) in enumerate(most_frequent_words):
        print("{}. {}: {}".format(index + 1, word, frequency))


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
