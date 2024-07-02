def fibonacci_if(i: int) -> int:
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci_if(i - 1) + fibonacci_if(i - 2)


def fibonacci_if_golf(i: int) -> int:
    if i > 1:
        return fibonacci_if_golf(i - 1) + fibonacci_if_golf(i - 2)
    else:
        return i


def fibonacci_match(i: int) -> int:
    match i:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibonacci_match(i - 1) + fibonacci_match(i - 2)


print([fibonacci_if(x) for x in range(10)])
print([*map(fibonacci_if_golf, range(10))])
print([*map(fibonacci_match, range(10))])
