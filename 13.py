import time
from aocd.models import Puzzle
import numpy as np

day, year = 13, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    inner = []
    for line in data.splitlines():
        if line == "":
            res.append(inner)
            inner = []
        else:
            inner.append(line)
    res.append(inner)
    return res


def check_reflection(pattern, i):
    j = 0
    while 0 <= i - j and j + i + 1 < len(pattern):
        if list(pattern[i + j + 1]) != list(pattern[i - j]):
            return False
        j += 1
    return True


def get_reflection_points(pattern):
    for i, line in enumerate(pattern[:-1]):
        if list(line) == list(pattern[i + 1]):
            if check_reflection(pattern, i):
                return i + 1
    return 0


def p1(data):
    rows = 0
    cols = 0
    for pattern in data:
        pattern = np.array([list(line) for line in pattern])
        rotated = np.rot90(pattern, k=3)

        r1 = get_reflection_points(rotated)
        r2 = get_reflection_points(pattern)
        cols += r1
        rows += r2

    return rows * 100 + cols


def check_smudged(pattern, i, smudged=False):
    j = 1
    while 0 <= i - j and j + i + 1 < len(pattern):
        cmp = sum(x != y for x, y in zip(pattern[i + j + 1], pattern[i - j]))
        if (smudged and cmp > 0) or cmp > 1:
            return False
        elif not smudged and cmp == 1:
            smudged = True
        j += 1
    return smudged


def get_smudged_points(pattern):
    for i, line in enumerate(pattern[:-1]):
        cmp = sum(x != y for x, y in zip(line, pattern[i + 1]))
        if cmp <= 1 and check_smudged(pattern, i, smudged=cmp):
            return i + 1
    return 0


def p2(data):
    rows = 0
    cols = 0
    for pattern in data:
        pattern = np.array([list(line) for line in pattern])
        rotated = np.rot90(pattern, k=3)

        r1 = get_smudged_points(rotated)
        r2 = get_smudged_points(pattern)
        cols += r1
        rows += r2
    return rows * 100 + cols


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
