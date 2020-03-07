def foo(character, filepath="files/bear.txt"):
    myfile = open(filepath)
    content = myfile.read()
    return content.count(character)

print(foo("e"))

''' Output
py -3 .\fileProcessingInFunc.py
56
'''
