a = 1
b = "2"
c = 3
print(int(2.5))
print(c/0)

## Output
# C:\Users\Rob\Desktop\AWS EC2\python-mega\Section18>py errors3.py
# 2
# Traceback (most recent call last):
#   File "errors3.py", line 5, in <module>
#     print(c/0)
# ZeroDivisionError: division by zero

# So Web Search of "ZeroDivisionError: division by zero" found:
# https://stackoverflow.com/questions/29836964/error-python-zerodivisionerror-division-by-zero
# This shows:

# Catch the error and handle it:

# try:
#     z = x / y
# except ZeroDivisionError:
#     z = 0
# Or check before you do the division:

# if y != 0:
#     z = x / y
# else:
#     z = 0
# The latter can be reduced to:

# z = (x / y) if y != 0 else 0