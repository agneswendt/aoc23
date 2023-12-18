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


def flood_fill(grid, curr, visited=set()):
    stack = [curr]
    while stack:
        curr = stack.pop()
        if curr in grid or curr in visited:
            continue
        visited.add(curr)
        x, y = curr
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))
    return visited


def p1(data):
    curr = (0, 0)
    digged = {curr}
    for elem in data:
        dir, val, _ = elem
        x, y = curr
        match dir:
            case "R":
                for i in range(val):
                    digged.add((x + i, y))
                curr = (x + val, y)
            case "L":
                for i in range(val):
                    digged.add((x - i, y))
                curr = (x - val, y)
            case "U":
                for i in range(val):
                    digged.add((x, y - i))
                curr = (x, y - val)
            case "D":
                for i in range(val):
                    digged.add((x, y + i))
                curr = (x, y + val)
        digged.add(curr)
    fill = flood_fill(digged, (-1, -61))
    return len(fill) + len(digged)


def p2(data):
    digged = []
    curr = (0, 0)

    for elem in data:
        dir, val, hex = elem
        val = int(hex[1:-1], 16)
        dir = hex[-1]
        x, y = curr
        match dir:
            case "0":  # R
                digged.append((curr, (x + val, y)))
                curr = (x + val, y)
            case "1":  # D
                digged.append((curr, (x, y + val)))
                curr = (x, y + val)
            case "2":  # L
                digged.append((curr, (x - val, y)))
                curr = (x - val, y)
            case "3":  # U
                digged.append((curr, (x, y - val)))
                curr = (x, y - val)

    area = 0
    for i in range(len(digged)):
        x1, y1 = digged[i][0]
        x2, y2 = digged[i][1]
        area += x1 * y2 - x2 * y1
        area += abs(x1 - x2) + abs(y1 - y2)
    return abs(area) // 2 + 1


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
