import time
from aocd.models import Puzzle
from collections import defaultdict
from heapq import heappush, heappop


day, year = 17, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def calc_cost(data, curr, dx, dy):
    cost = 0
    if dx > 0:
        for i in range(1, dx + 1):
            cost += int(data[curr[1]][curr[0] + i])
    elif dx < 0:
        for i in range(-1, dx - 1, -1):
            cost += int(data[curr[1]][curr[0] + i])
    if dy > 0:
        for i in range(1, dy + 1):
            cost += int(data[curr[1] + i][curr[0]])
    elif dy < 0:
        for i in range(-1, dy - 1, -1):
            cost += int(data[curr[1] + i][curr[0]])
    return cost


def solve(data, generator):
    start_dir = (0, 0)
    start = (0, 0)
    end = (len(data[0]) - 1, len(data) - 1)
    Q = []
    heappush(Q, (0, start, start_dir))
    visited = set()
    costs = defaultdict(lambda: float("inf"))
    costs[start] = 0
    while Q:
        cost, curr, prev_dir = heappop(Q)
        if (curr, prev_dir) in visited:
            continue
        if curr == end:
            return cost
        visited.add((curr, prev_dir))
        x, y = curr
        for dx, dy in generator(prev_dir):
            if not (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data)):
                continue
            r_cost = calc_cost(data, curr, dx, dy)
            n_cost = r_cost + cost
            heappush(Q, (n_cost, (x + dx, y + dy), (dx, dy)))
    assert False


def p1(data):
    def gen(dir):
        res = set()
        if 1 <= abs(dir[0]) <= 3:
            for x in range(1, 4):
                res.add((0, x))
                res.add((0, -x))
        elif 1 <= abs(dir[1]) <= 3:
            for y in range(1, 4):
                res.add((y, 0))
                res.add((-y, 0))
        else:
            for xy in range(1, 4):
                res.add((0, xy))
                res.add((xy, 0))
        return res

    return solve(data, gen)


def p2(data):
    def gen(dir):
        res = set()
        if 4 <= abs(dir[0]) <= 10:
            for x in range(4, 11):
                res.add((0, x))
                res.add((0, -x))
        elif 4 <= abs(dir[1]) <= 10:
            for y in range(4, 11):
                res.add((y, 0))
                res.add((-y, 0))
        else:
            for xy in range(4, 11):
                res.add((0, xy))
                res.add((xy, 0))
        return res

    return solve(data, gen)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
