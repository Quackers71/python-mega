def mean(mylist):
    print("Function started!")
    the_mean = sum(mylist) / len(mylist)
    return the_mean

mymean = mean([0, 3, 4])
print(mymean)

#print(mean([1, 4, 5, 9, 300]))

#print("mean = ",type(mean) , "  sum =",type(sum), "  len = ",type(len))
