mydict = ["name":"John", "surname":"Smith"] 
print(mydict)

## Output
# C:\Users\Rob\Desktop\AWS EC2\python-mega\Section18>py question1.py
#   File "question1.py", line 1
#     mydict = ["name":"John", "surname":"Smith"]
#                     ^
# SyntaxError: invalid syntax

# A SyntaxError would be generated because when you start with square brackets 
# Python thinks you are about to define a list, but then you use colons instead 
# of commas so that is not the correct syntax to define a list, thus the SyntaxError.