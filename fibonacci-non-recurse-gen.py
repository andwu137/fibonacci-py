from itertools import islice


def fibs():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y


print([*islice(fibs(), 10)])
