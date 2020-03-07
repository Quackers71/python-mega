def foo(*args):
    return sum(args) / len(args)

print(int(foo(10, 20, 30, 40)))