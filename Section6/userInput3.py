# Two methods of string formatting

name = input("Enter your first name: ")
surname = input("Enter your surname: ")
when = "today"
#message = "Hello %s %s, what's up %s" % (name, surname, when)
message = f'Hello {name} {surname}, {when}'
print(message)
