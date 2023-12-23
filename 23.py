import time
from aocd.models import Puzzle
from collections import defaultdict


day, year = 23, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def build_graph(data, start, end, dir_gen):
    graph = {}

    def inner(start, end, prev_dir=(0, 1)):
        curr = start
        visited = set()
        first = True
        while curr:
            x, y = curr
            visited.add(curr)
            if curr == end:
                graph[(start, prev_dir)] = (curr, len(visited) - 1)
                return
            iter_dirs = (prev_dir,) if first else dir_gen[data[y][x]]
            first = False
            dirs = []
            for dx, dy in iter_dirs:
                if not (data[y + dy][x + dx] == "#" or (x + dx, y + dy) in visited):
                    dirs.append((dx, dy))
            if len(dirs) == 0:
                return
            elif len(dirs) == 1:
                curr = (x + dirs[0][0], y + dirs[0][1])
            else:
                graph[(start, prev_dir)] = (curr, len(visited) - 1)
                for dir in dirs:
                    if (curr, dir) not in graph:
                        inner(curr, end, dir)
                return

    inner(start, end)
    return graph


def traverse(graph, start, goal):
    S = [(start, frozenset(), 0)]
    costs = []
    while S:
        curr, visited, cost = S.pop()
        if curr == goal:
            costs.append(cost)
            continue
        for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (curr, dir) not in graph:
                continue
            end, steps = graph[(curr, dir)]
            if end in visited:
                continue
            vis = visited | {end}
            S.append((end, vis, cost + steps))
    return max(costs)


def p1(data):
    for x in range(len(data[0])):
        if data[0][x] == ".":
            start = (x, 0)
        if data[-1][x] == ".":
            end = (x, len(data) - 1)
    dirs = {
        "^": ((0, -1),),
        "v": ((0, 1),),
        "<": ((-1, 0),),
        ">": ((1, 0),),
        ".": ((0, 1), (0, -1), (1, 0), (-1, 0)),
    }
    graph = build_graph(data, start, end, dirs)
    return traverse(graph, start, end)


def p2(data):
    for x in range(len(data[0])):
        if data[0][x] == ".":
            start = (x, 0)
        if data[-1][x] == ".":
            end = (x, len(data) - 1)
    dirs = defaultdict(lambda: ((0, 1), (0, -1), (1, 0), (-1, 0)))
    graph = build_graph(data, start, end, dirs)
    return traverse(graph, start, end)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
