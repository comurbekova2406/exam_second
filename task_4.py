def func(*args):

    summ = 0
    for i in args:
        if isinstance(i, (int, float)):
            summ += i
    return summ


print(func(5, 1, 7))
