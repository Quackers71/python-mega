# use the json modules
import json

# Creating the File Object using the open("File_Path") method
data = json.load(open("data.json"))

''' create the translate function and return 'data[w]'
    'w' is a Local variable '''
def translate(w):
    return data[w]

#use the 'word' Global variable for the input function
word = input("Enter a word: ")

# printout using the translate function of the Global varaible 'word' input
print(translate(word))

