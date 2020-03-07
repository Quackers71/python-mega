def foo(lst):
    return [i for i in lst if not isinstance(i, str)]

foo([99, 'no data', 95, 94, 'no data'])


