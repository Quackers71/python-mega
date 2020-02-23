def mean(mylist):
    print("Function started!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean

student_grades = {"Kylie": 9.1, "Eva": 8.8, "Tarquin": 7.5}
print(mean(student_grades))
