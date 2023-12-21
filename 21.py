import time
from aocd.models import Puzzle
import numpy as np


day, year = 21, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def add_tuples(a, b):
    return a[0] + b[0], a[1] + b[1]


def calc_steps(map, start, s=64):
    queue = [(start, 0)]
    visited = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0
    while queue:
        curr, steps = queue.pop(0)
        if curr in visited or steps > s:
            continue
        if s % 2 == 0 and steps % 2 == 0:
            res += 1
        elif s % 2 == 1 and steps % 2 == 1:
            res += 1
        visited.add(curr)
        for dir in dirs:
            new = add_tuples(curr, dir)
            nx, ny = new
            nx, ny = nx % len(map[0]), ny % len(map)
            if map[ny][nx] != "#":
                queue.append((new, steps + 1))
    return res


def p1(data):
    start = (65, 65)
    return calc_steps(data, start, s=64)


def p2(data):
    num = 26501365
    width = len(data)
    start = (65, 65)

    y_vals = []
    for step in range(1, 6, 2):
        y_vals.append(calc_steps(data, start, s=step * width // 2))

    x_vals = np.array([0, 1, 2])
    y_vals = np.array(y_vals)
    a, b, c = np.polyfit(x_vals, y_vals, 2)
    n = num // width
    return int(a * n**2 + b * n + c)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
