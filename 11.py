import time
from aocd.models import Puzzle


day, year = 11, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def solve(data, amp=2):
    galaxies = []
    rows, cols = set(), set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))
                rows.add(x)
                cols.add(y)
    res = 0
    for i, (x1, y1) in enumerate(galaxies):
        for x2, y2 in galaxies[i + 1 :]:
            x_rep = len(set(range(min(x1, x2), max(x1, x2) + 1)) - rows) * (amp - 1)
            y_rep = len(set(range(min(y1, y2), max(y1, y2) + 1)) - cols) * (amp - 1)

            res += abs(x2 - x1) + abs(y2 - y1) + x_rep + y_rep
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = solve(data)
    p2 = solve(data, amp=1000000)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
