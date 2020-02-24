def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)    
    else: 
        the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Kylie": 9.1, "Eva": 8.8, "Tarquin": 7.5}

print("mean(student_grades) :",mean(student_grades))

if 3 > 1:
    print("3 is greater than 1")
else:
    print("Not Greater")

print("type(3) == int :",type(3) == int)

print("isinstance(3, int) :",isinstance(3, int))
