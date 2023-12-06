import time
from aocd.models import Puzzle
from functools import cache


day, year = 6, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        if "Time" in line:
            times = list(
                map(int, filter(lambda x: x.isdigit(), line.split(": ")[1].split()))
            )
        if "Distance" in line:
            distances = list(
                map(int, filter(lambda x: x.isdigit(), line.split(": ")[1].split()))
            )

    return (times, distances)


@cache
def traverse(time, record, held):
    if time == 0:
        return 0
    elif held * time > record:
        return 1 + traverse(time - 1, record, held + 1)
    else:
        return traverse(time - 1, record, held + 1)


def p1(data):
    print(data)
    times, record = data
    res = 1
    for t, d in zip(times, record):
        res *= traverse(t, d, 0)
    return res


def p2(data):
    t, d = data
    t = int("".join(map(str, t)))
    d = int("".join(map(str, d)))
    res = 0
    held = 0
    while t > 0:
        if t * held > d:
            res += 1
        held += 1
        t -= 1
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
