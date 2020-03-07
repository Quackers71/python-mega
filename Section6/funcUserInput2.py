def foo(name):
    return "Hi %s!" % name.title()


inputName = input("Enter your name: ")

print(foo(inputName))
