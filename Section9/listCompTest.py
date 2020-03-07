def foo(lst):
    nums = []
    for i in lst: 
        if not isinstance(i, str):
            nums.append(i)
            print(i)
    return nums

foo([99, 'no data', 95, 94, 'no data'])

""" For comparison, here is a different way to solve this quiz-challenge. 
It uses both a for-loop and an if-test. The solution loops and appends 
only the numeric values from lst to a 2nd list variable that I've named nums: """
