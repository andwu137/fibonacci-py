from typing import Callable, TypeVar


A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
type F1T1[A, B] = Callable[[A], B]
type F2T1[A, B, C] = Callable[[A, B], C]


def memofix_dict[A, B](f: F2T1[F1T1[A, B], A, B]) -> F1T1[A, B]:
    xs: dict[A, B] = dict()

    def fP(x):
        nonlocal xs
        if x not in xs:
            xs[x] = f(fP, x)
        return xs[x]

    return fP


def memofix_list[A](f: F2T1[F1T1[int, A], int, A]) -> F1T1[int, A]:
    xs: list[A] = []

    def fP(x: int) -> A:
        nonlocal xs
        if len(xs) - 1 < x:
            xs.insert(x, f(fP, x))
        return xs[x]

    return fP


def fibonacci_fix(f: F1T1[int, int], i: int) -> int:
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return f(i - 1) + f(i - 2)


print([*map(memofix_list(fibonacci_fix), range(10))])
print([*map(memofix_dict(fibonacci_fix), range(10))])
