mylist = [John, Jack, Jim] 
print(mylist)

## Output
# C:\Users\Rob\Desktop\AWS EC2\python-mega\Section18>py question4.py
# Traceback (most recent call last):
#   File "question4.py", line 1, in <module>
#     mylist = [John, Jack, Jim]
# NameError: name 'John' is not defined

# You would get a NameError again because John, Jack, and Jim names were not 
# defined in the script. So, as soon as Python detects that John was not defined, 
# it interrupts the code with a NameError and it doesn't even check the rest of 
# the code.