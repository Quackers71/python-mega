def foo(name):
    return "Hi %s!" % name.title()


inputName = raw_input("Enter your name: ")

print(foo(inputName))
