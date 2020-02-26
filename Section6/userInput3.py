# Two methods of string formatting

name = raw_input("Enter your first name: ")
surname = raw_input("Enter your surname: ")
when = "today"
message = "Hello %s %s, what's up %s" % (name, surname, when)
#message = f'Hello {name} {surname}'
print(message)
