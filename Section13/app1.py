# use the json modules and from difflib import g_c_m
import json
from difflib import get_close_matches

# Creating the File Object using the open("File_Path") method
data = json.load(open("data.json"))

''' create the translate function and return 'data[w]'
    'w' is a Local variable '''
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    # If the user entered "dog" this will check for "Dog" as well.
    elif w.title() in data:
        return data[w.title()]
    # Check the length of the close match and is greater than 0
    elif len(get_close_matches(w, data.keys())) > 0:
        # Ask User for close word
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn.capitalize() == "Y":
            # if Y(yes) return the word
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.capitalize() == "N":
            # else if N(no) return don't exist!
            return "The word doesn't exist!  Please double check it..."
        else:
            # else You crap!
            return "We didn't understand your entry."
    else:
        # No matches!
        return "The word doesn't exist!  Please double check it..."

#use the 'word' Global variable for the input function
word = input("Enter a word: ")

# Iterate through the List Object (if it is a List otherwise print output)
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
