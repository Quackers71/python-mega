# use the json modules
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
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word doesn't exist!  Please double check it..."

#use the 'word' Global variable for the input function
word = input("Enter a word: ")

# printout using the translate function of the Global varaible 'word' input
print(translate(word))
