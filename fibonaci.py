from typing import Callable, Any

type A = Any
type B = Any
type C = Any
type Predicate3 = Callable[[A], Callable[[B], Callable[[C], bool]]]
type Merge3 = Callable[[A], Callable[[B], Callable[[C], int]]]
type F = Callable[
    [Predicate3],
    Callable[
        [Merge3],
        Callable[
            [Merge3],
            Callable[
                [Merge3],
                Callable[[F], Callable[[int], Callable[[int], Callable[[int], int]]]],
            ],
        ],
    ],
]


# Constructs a fix-point combinator function `f` using the provided predicate.
#
# Args:
#     predicate (Predicate3): A predicate function that takes three arguments
#     of any type (`A`, `B`, `C`) and returns a boolean.
#
# Returns:
#     F: A fix-point combinator function `f`.
f: F = (
    lambda predicate:
        (lambda x_prime:
            (lambda y_prime:
                (lambda z_prime:
                    (lambda fix_point_recurse:
                        (lambda x:
                            (lambda y:
                                (lambda z: (
                                    (fix_point_recurse
                                        (predicate)
                                        (x_prime)
                                        (y_prime)
                                        (z_prime)
                                        (fix_point_recurse)
                                        (x_prime
                                         (x)
                                         (y)
                                         (z))
                                        (y_prime
                                         (x)
                                         (y)
                                         (z))
                                        (z_prime
                                         (x)
                                         (y)
                                         (z)))
                                    if not (predicate
                                            (x)
                                            (y)
                                            (z))
                                    else x
                                )))))))))


# Returns a function that always returns the constant value `x`.
#
# Args:
#     x (A): The constant value.
#
# Returns:
#     Callable[[B], A]: A function that takes any argument and returns `x`.
const: Callable[[A], Callable[[B], A]] = lambda x: lambda _: x

# Returns a function that flips the order of arguments to function `f`.
#
# Args:
#     f (Callable[[A], B]): The function to flip.
#
# Returns:
#     Callable[[B], A]: A function that takes the second argument first
#                       and then the first argument.
flip: Callable[[Callable[[A], B]], Callable[[B], A]] = lambda f: (
    lambda b: lambda a: f(a)(b)
)

# Returns the input
#
# Args:
#     x A: The input to return
#
# Returns:
#     A: The input that is returned
id: Callable[[A], A] = lambda x: x

# Returns a function that composes two functions.
#
# Args:
#     f (Callable[[B], C]): The outer function to apply.
#
# Returns:
#     Callable[[Callable[[A], B]], Callable[[A], C]]:
#               A function that applies `f` after `g`.
dot: Callable[[Callable[[B], C]], Callable[[Callable[[A], B]], Callable[[A], C]]] = (
    lambda f: lambda g: lambda x: f(g(x))
)

dot3 = lambda f: lambda g: lambda x: lambda y: lambda z: f(g(x)(y)(z))


add: Callable[[int], Callable[[int], int]] = lambda x: lambda y: x + y
zero: int = 0
one: int = 1


# Computes the Fibonacci number for a given index
# using the fix-point combinator `f`.
#
# Args:
#     i (int): Index of the Fibonacci number to compute.
#
# Returns:
#     int: The Fibonacci number at index `i`.
fibonacci: Callable[[int], int] = lambda i: (
    f(dot3(i.__eq__)(const(const(id))))(dot(const(const))(id))(
        dot(dot)(dot)(const)(add)
    )(dot3(one.__add__)(const(const(id))))(f)(zero)(one)(zero)
)


print([*map(fibonacci, range(100))])
