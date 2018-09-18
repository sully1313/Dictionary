import json

from difflib import get_close_matches

replay = "y"
while replay == "y":

    data = json.load(open("data.json", 'r'))

    def translate (w):
        w = w.lower()
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter (Y/N): " % get_close_matches(w, data.keys())[0])
            yn = yn.upper()
            if yn == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry"
        else:
            return "The word doesn't exist. Please double check it."

    word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    replay = str(input("Would you like to rerun this program(Y/N): "))
    replay = replay.lower()
exit()
