def foo(lst):
    nums = []
    for i in lst:     
        print(sum(float(i) for i in lst))
        print(type(i))
      
    return nums

foo(['1.2', '2.6', '3.3'])