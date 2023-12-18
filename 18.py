import time
from aocd.models import Puzzle
from collections import defaultdict


day, year = 18, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    res = []
    for line in data.splitlines():
        dir, val, hex = line.split()
        val = int(val)
        hex = hex[1:-1]
        res.append((dir, val, hex))
    return res


def calc_term(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return x1 * y2 - x2 * y1 + abs(x1 - x2) + abs(y1 - y2)


def p1(data):
    area = 0
    curr = (0, 0)
    for elem in data:
        dir, val, _ = elem
        x, y = curr
        match dir:
            case "R":
                next = (x + val, y)
            case "L":
                next = (x - val, y)
            case "U":
                next = (x, y - val)
            case "D":
                next = (x, y + val)
        area += calc_term(curr, next)
        curr = next
    return area // 2 + 1


def p2(data):
    area = 0
    curr = (0, 0)
    for elem in data:
        _, _, hex = elem
        val = int(hex[1:-1], 16)
        dir = hex[-1]
        x, y = curr
        match dir:
            case "0":  # R
                next = (x + val, y)
            case "1":  # D
                next = (x, y + val)
            case "2":  # L
                next = (x - val, y)
            case "3":  # U
                next = (x, y - val)
        area += calc_term(curr, next)
        curr = next

    return abs(area) // 2 + 1


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
