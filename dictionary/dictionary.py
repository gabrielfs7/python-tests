import json
from difflib import SequenceMatcher, get_close_matches

with open("storage.json", "r") as json_file:
    data = json.load(json_file)


def show_description(data, keyword):
    for description in data[keyword]:
        print(" " + description)

"""
Search for keyword in the dictionary or suggest new words based on similarity.
"""
while True:
    keyword = input("\nWhat are you looking for: ").lower()

    try:
        show_description(data, keyword)
    except KeyError as error:
        dic = {}
        keyword_suggestion = None
        max_matches_to_return = 1

        for match in get_close_matches(keyword, data.keys(), max_matches_to_return, 0.0):
            ratio = SequenceMatcher(None, keyword, match).ratio() * 100
            keyword_suggestion = match

        if keyword_suggestion is None:
            print(" - Could not find any fruit.")
        else:
            answer = input(" - Did you mean '%s' (ratio of %2.2f percent) ? Type 'Y' to proceed: " % (keyword_suggestion, ratio)).lower()

            if answer == 'y':
                show_description(data, keyword_suggestion)