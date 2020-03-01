#Keyword Args defined
def area(a=5, b=7):
    return a * b

print(area(a=4, b=7))

# default Args
def area(a, b=7):
    return a * b

print(area(5))

# function call will override keyword Args
def area(a=10, b=9):
    return a * b

print(area(150, 50))

# This won't work
""" def area(a=5, b):
    return a * b

print(area(4, 5)) """

# Output
'''  File ".\moreOnfuncArgs.py", line 14
    def area(a=5, b):
             ^
SyntaxError: non-default argument follows default argument'''