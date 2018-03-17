"""
Different version for dictionary search
"""
import json
from difflib import get_close_matches

data = json.load(open("storage.json"))


def translate(w):
    if w.title() in data:
        return data[w.title()]

    if w.lower() in data:
        return data[w.lower()]

    if w.upper() in data:
        return data[w.upper()]

    close_matches = get_close_matches(w, data.keys());

    if len(close_matches) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % close_matches[0])

        if yn == "Y":
            return data[close_matches[0]]

        if yn == "N":
            return "The word doesn't exist. Please double check it."

        return "We didn't understand your entry."

    return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
