#!/usr/bin/env python3
"""Choose and pretty-print a random verse of scripture."""
# pylint: disable=C0103
import json
import random
import textwrap

file_path = "lds-scriptures.json"
#file_path = "this.json"
def get_random_verse(filter_book = None):
    """Pick a random verse."""

    with open(file_path, "r") as scripture_file:
        verse_list = json.load(scripture_file)
        if filter_book:
            filter_list = [token for token in verse_list if token['volume_id'] == filter_book]
        else :
            filter_list = verse_list
        verse = random.choice(filter_list)

    return verse


def pretty_print_verse(verse):
    """Given a verse in dictionary form, return a nice-looking string."""
    to_return = verse["verse_title"]
    to_return += ": \n"
    wrapped_verse = textwrap.wrap(verse["scripture_text"])
    for line in wrapped_verse:
        to_return += line + "\n"
    to_return += generate_scripture_url(verse)
    return to_return


def generate_scripture_url(verse):
    """Generate a verse's churchofjesuschrist url."""
    to_return = "https://www.churchofjesuschrist.org/study/scriptures/"
    if verse["volume_lds_url"] == "bm":
        to_return += "bofm"
    elif verse["volume_lds_url"] == "dc":
        to_return += "dc-testament"
    else:
        to_return += verse["volume_lds_url"]
    to_return += "/" + verse["book_lds_url"]
    to_return += "/" + str(verse["chapter_number"])
    to_return = to_return + "." + str(verse["verse_number"]) + "?lang=eng#"
    if verse["verse_number"] == 1:
        return to_return + "p1"
    return to_return + str(verse["verse_number"] - 1)


if __name__ == "__main__":
    rand_verse = get_random_verse()
    print("Random verse: ")
    print(pretty_print_verse(rand_verse))
