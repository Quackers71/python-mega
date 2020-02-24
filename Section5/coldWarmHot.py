def foo(temp):
    if temp > 25:
        return "Hot"
    elif 25 >= temp >= 15:
        return "Warm"
    else:
        return "Cold"

foo(14)
print(foo(14))
