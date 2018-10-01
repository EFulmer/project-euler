import itertools


def fibonacci_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def digit_count(n: int) -> int:
    return len(str(n))


def digit_count_enumerate(t: tuple) -> int:
    return len(str(t[1]))


def less_than_1000_digits(t: tuple) -> bool:
    return digit_count_enumerate(t) < 1000


def problem_031():
    fibonacci_numbers_with_indices = enumerate(fibonacci_gen())
    gen = itertools.dropwhile(
        less_than_1000_digits, fibonacci_numbers_with_indices
    )
    index, number = next(gen)
    print(index + 1)


if __name__ == '__main__':
    problem_031()
