def foo(lst):
    nums = []
    for i in lst: 
        if i > 0:
            nums.append(i)
            print(i)

foo([-5, 3, -1, 101])