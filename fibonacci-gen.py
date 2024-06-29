from itertools import islice
from operator import add


def fibs():
    yield 0
    yield 1
    for x in map(add, fibs(), islice(fibs(), 1, None)):
        yield x


print([*islice(fibs(), 10)])
