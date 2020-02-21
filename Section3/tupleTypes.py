def cr():
    print("\r")

print("This is a Tuple")
print("monday_temperatures = {1, 4, 5}")
monday_temperatures = {1, 4, 5}
print(monday_temperatures)
cr()

print("This is a List")
print("monday_temperatures2 = [1, 4, 5]")
monday_temperatures2 = [1, 4, 5]
print(monday_temperatures2)
cr()

monday_temperatures2.append(9)
print("monday_temperatures2.append(9)")
print("The List is now: ",monday_temperatures2)
cr()

print("This is a Dictonary")
print('monday_temperatures3 = {"temp1": 1, "temp2": 4, "temp3": 5}')
monday_temperatures3 = {"temp1": 1, "temp2": 4, "temp3": 5}
print(monday_temperatures3)
cr()

print("output of the dict.values in a for loop")
for i in monday_temperatures3.values():
    print(i)
