def foo(lst):
    nums = []
    for i in lst:     
        print(sum(float(i) for i in lst))
        print(type(i))
      
    return nums

print(foo([1.2, 2.6, 3.3]))