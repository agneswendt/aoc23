import time
from aocd.models import Puzzle
from math import ceil

day, year = 10, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


mapping = {
    (0, 1): "|LJS",
    (0, -1): "|7FS",
    (1, 0): "-7JS",
    (-1, 0): "-FLS",
}
allowed = {
    "S": {(0, 1), (0, -1), (1, 0), (-1, 0)},
    "F": {(0, 1), (1, 0)},
    "J": {(0, -1), (-1, 0)},
    "L": {(0, -1), (1, 0)},
    "7": {(0, 1), (-1, 0)},
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
}


def is_valid_step(coords, step, data):
    x, y = coords
    dx, dy = step
    curr = data[y][x]
    next = data[y + dy][x + dx]
    if not (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data)):
        return False
    return step in allowed[curr] and next in mapping[step]


def traverse(start, data):
    x, y = start
    visited = {start}
    Q = [start]
    while Q:
        curr = Q.pop(0)
        x, y = curr
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if not (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data)):
                continue
            if (x + dx, y + dy) in visited or data[y + dy][x + dx] == ".":
                continue
            if is_valid_step(curr, (dx, dy), data):
                Q.append((x + dx, y + dy))
                visited.add((x + dx, y + dy))
    return visited


def p1(data):
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                return ceil(len(traverse((x, y), data)) / 2)


def check_dir(coords, data, visited, step):
    x, y = coords
    dx, dy = step
    last = None
    left, right = 0, 0
    res = 0
    while 0 < x < len(data[0]) - 1 and 0 < y < len(data) - 1:
        x += dx
        y += dy

        if (x, y) in visited:
            if last is None or not is_valid_step(last, step, data):
                res += left % 2 == 1 and right % 2 == 1
                left, right = 0, 0
            if step[1] == 0:
                left += is_valid_step((x, y), (0, -1), data)
                right += is_valid_step((x, y), (0, 1), data)
            else:
                left += is_valid_step((x, y), (-1, 0), data)
                right += is_valid_step((x, y), (1, 0), data)
            last = (x, y)
    res += left % 2 == 1 and right % 2 == 1
    return res


def is_enclosed(coords, data, visited):
    for dir in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        if check_dir(coords, data, visited, dir) % 2 == 0:
            return False
    return True


def p2(data):
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
                visited = traverse(start, data)
                break
        else: continue
        break

    res = 0
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if (x, y) not in visited:
                if is_enclosed((x, y), data, visited):
                    res += 1
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
