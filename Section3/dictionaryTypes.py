def cr():
    print("\r")

monday_temperatures = [9.1, 8.8, 7.5]
print("Monday Temperatue is:",monday_temperatures[0])
mysum = sum(monday_temperatures)
print("sum(monday_temperatures) : ",mysum)
length = len(monday_temperatures)
print("len(monday_temperatures) : ", length)
mean = mysum / length
print("The mean of the monday_temperatures : ", mean)
cr()

student_grades = {"Mary": 9.1, "Sim": 6.8, "John": 9.9} # dict have keys & values i.e. "key": value,  
print(student_grades.keys())
print(student_grades.values())

mysum2 = sum(student_grades.values())
print("sum(student_grades.values() : ",mysum2)
