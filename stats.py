"""Statistics module for the Bookbot project."""

def get_num_words(contents):
    """Counts the number of words in the provided string."""
    return len(contents.split())


def get_char_counts(contents):
    """Determine individual character counts.

    Deduplicate by converting all appropriate characters to lowercase.
    """
    counts = {}
    for character in contents:
        char = character.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def sort_by(dct):
    """Returns the value to sort by."""
    return dct["count"]


def sort_char_counts(char_dict):
    """Converts dictionary of char counts to sorted list of dictionaries.

    Each dictionary has a char and a count key.
    """
    char_dicts = [{"char": key, "count": val} for key, val in char_dict.items() if key.isalpha()]
    char_dicts.sort(reverse=True, key=sort_by)
    return char_dicts
