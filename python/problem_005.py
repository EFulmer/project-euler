import itertools


def divisible_by_first_n(n: int, x: int) -> bool:
    first_n = range(1, n+1)
    divisible_by_x = [x % m != 0 for m in first_n]
    return all(divisible_by_x)


def divisible_by_1_to_20(x: int) -> bool:
    return divisible_by_first_n(20, x)


def problem_005():
    count = itertools.count(start=21, step=1)
    x = itertools.dropwhile(divisible_by_1_to_20, count)
    print(next(x))


if __name__ == '__main__':
    problem_005()
