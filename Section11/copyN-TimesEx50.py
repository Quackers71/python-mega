with open("files/data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write("\n"+content)
    file.write("\n"+content)

print(content)