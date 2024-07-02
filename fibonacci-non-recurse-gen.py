from itertools import islice
from typing import Generator


def fibs() -> Generator[int, None, None]:
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


print([*islice(fibs(), 10)])
