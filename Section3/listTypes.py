x = 10
y = '10'
z = 10.1

sum1 = x + x
sum2 = y + y

#print(sum1, sum2)
#print(type(x), type(y), type(z))

myList = [x, y, z]
for i in myList:
    print(type(i))

for i in myList:
    print(i)

for i in myList:
    print(hash(i))
    
for i in myList:
    print(ascii(i))
