import re
import sys
from collections import defaultdict
from pprint import pprint


def load_text(filepath):
    with open(filepath) as text_file:
        text = text_file.read()
        return text


def get_most_frequent_words(text):
    text = re.sub(r"\W", " ", text)
    words = text.lower().split()
    frequency_by_word = defaultdict(lambda: 0)
    for word in words:
        frequency_by_word[word] += 1

    top_ten_frequent_words = sorted(
        frequency_by_word.items(), key=lambda item: item[1], reverse=True
    )[:10]
    return top_ten_frequent_words


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No filepath argument")

    filepath = sys.argv[1]
    try:
        text = load_text(filepath)
        top_ten_frequent_words = get_most_frequent_words(text)
        pprint(top_ten_frequent_words)
    except FileNotFoundError:
        sys.exit("File not found")
