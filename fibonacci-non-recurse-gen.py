from itertools import islice


def fibs():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


print([*islice(fibs(), 10)])
