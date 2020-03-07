with open("files/bear.txt", "r") as file:
    content = file.read()

with open("files/first90.txt", "w") as file:
    file.write(content[:90])

with open("files/first90.txt", "r") as file:
    content = file.read()
    print(content)