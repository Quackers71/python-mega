address = ["Flat Floor Street", "18", "New York"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(address[0], address[1])

pin = int(input("Enter your pin: "))


def find_in_file(f):    
    myfile = open("sample2.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That fruit is in the list."
    else:
        return "No such fruit found!"


def print_list_in_file():
    myfile = open("sample2.txt", "r")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    print(fruits)
    myfile.close()


if pin in pins.values():

    print_list_in_file()

    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!") 
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)
