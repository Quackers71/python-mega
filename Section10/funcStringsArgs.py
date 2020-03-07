def foo(*args):
    args = [i.upper() for i in args]
    return  sorted(args)

print(foo("snow", "glacier", "iceberg"))