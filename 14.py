import time
from aocd.models import Puzzle
from collections import defaultdict


day, year = 14, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(list(line))
    return res


def print_grid(grid):
    for line in grid:
        print("".join(line))


def p1(data):
    last = [0 for _ in range(len(data))]
    stones = set()
    for y, lst in enumerate(data):
        for x, c in enumerate(lst):
            if c == "#":
                last[x] = y + 1
            elif c == "O":
                stones.add((x, last[x]))
                last[x] += 1

    N = len(data)
    load = 0
    for _, y in stones:
        load += N - y
    return load


def add_tuples(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))


def sub_tuples(t1, t2):
    return tuple(x - y for x, y in zip(t1, t2))


def p2(data):
    moving = set()
    static = set()
    for y, lst in enumerate(data):
        for x, c in enumerate(lst):
            if c == "O":
                moving.add((x, y))
            elif c == "#":
                static.add((x, y))

    def move(x, y, dir):
        while True:
            x, y = add_tuples((x, y), dir)
            if (x, y) in static or (x, y) in moving:
                break
            elif x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
                break
        return sub_tuples((x, y), dir)

    def count(moving):
        N = len(data)
        load = 0
        for _, y in moving:
            load += N - y
        return load

    def detect_cycle(cache):
        for k in range(1, len(cache) // 2):
            if cache[-k:] == cache[-2 * k : -k]:
                return k
        return 0

    cache = []
    i = 0
    while i < 1000000000:
        for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ry = range(len(data)) if dir[1] < 0 else range(len(data) - 1, -1, -1)
            rx = range(len(data[0])) if dir[0] < 0 else range(len(data[0]) - 1, -1, -1)
            for y in ry:
                for x in rx:
                    if (x, y) not in moving:
                        continue
                    moving.remove((x, y))
                    moving.add(move(x, y, dir))
        c = count(moving)
        if c in cache:
            cycle = detect_cycle(cache)
            if cycle > 1:
                i += cycle * ((1000000000 - i) // cycle)
        cache.append(c)
        i += 1
    return c


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
