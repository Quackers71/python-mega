def mean(value):
    if type(value)  == dict:
        the_mean = sum(value.values()) / len(value)    
    else: 
        the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Kylie": 9.1, "Eva": 8.8, "Tarquin": 7.5}

print(mean(student_grades))
