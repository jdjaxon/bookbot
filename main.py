#!/usr/bin/env python3

"""Bookbot"""

import sys

from stats import (
    get_num_words,
    get_char_counts,
    sort_char_counts,
)


def main():
    """Generates Bookbot report."""
    if len(sys.argv) != 2:
        display_usage()
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")

    contents = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}")

    print("----------- Word Count ----------")
    word_count = get_num_words(contents)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(contents)
    sorted_counts = sort_char_counts(char_counts)
    for group in sorted_counts:
        char = group["char"]
        count = group["count"]
        print(f"{char}: {count}")

    print("============= END ===============")


def get_book_text(path):
    """Reads text from the provided text file."""

    with open(path, encoding="utf-8") as file:
        contents = file.read()
        return contents


def display_usage():
    """Displays program usage to the user."""
    print(f"Usage: python3 {sys.argv[0]} <path_to_book>")


if __name__ == "__main__":
    main()
