import time
from aocd.models import Puzzle
from itertools import product

day, year = 16, 2023

def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def sub_tuples(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])


def convert(c, dir):
    match c:
        case "|":
            if dir in ((1, 0), (-1, 0)):
                return [(0, 1), (0, -1)]
        case "-":
            if dir in ((0, 1), (0, -1)):
                return [(1, 0), (-1, 0)]
        case "/":
            return [sub_tuples((0, 0), (dir[1], dir[0]))]
        case "\\":
            return [(dir[1], dir[0])]
        case _:
            return [dir]
    return [dir]


def walk(grid, curr, dir):
    stepped = set()
    walked = set()
    x, y = curr
    stack = [((x, y), dir)]
    while stack:
        (x, y), dir = stack.pop()
        if not (x, y, dir) in stepped:
            stepped.add((x, y, dir))
            walked.add((x, y))
        else: continue

        dirs = convert(grid[y][x], dir)
        for d in dirs:
            new = add_tuples((x, y), d)
            if 0 <= new[0] < len(grid[0]) and 0 <= new[1] < len(grid):
                stack.append((new, d))
    return len(walked)


def p1(grid):
    return walk(grid, (0, 0), (1, 0))


def p2(grid):
    n, m = len(grid[0]), len(grid)
    x_values = [
        (0,),
        (n - 1,),
        tuple(range(n)),
        tuple(range(n)),
    ]
    y_values = [
        tuple(range(m)),
        tuple(range(m)),
        (0,),
        (m - 1,),
    ]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    res = 0
    for dir, (x_r, y_r) in zip(dirs, zip(x_values, y_values)):
        for x, y in product(x_r, y_r):
            res = max(res, walk(grid, (x, y), dir))
    return res



if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
