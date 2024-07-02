from typing import Generator
from itertools import islice
from operator import add


def fibs() -> Generator[int, None, None]:
    yield 0
    yield 1
    for x in map(add, fibs(), islice(fibs(), 1, None)):
        yield x


print([*islice(fibs(), 10)])
