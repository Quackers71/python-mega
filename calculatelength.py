
def length_of_string():
    user_input = input("Enter some Characters : ")
    mystring = user_input

    if type(mystring) == int:
        return "Sorry, integers don't have length"
    else:
        return len(mystring)


print(length_of_string())


def string_length(mystring):
    return len(mystring)


print(string_length("Hello World"))
