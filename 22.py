import time
from aocd.models import Puzzle
from copy import deepcopy
from collections import defaultdict

day, year = 22, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        a, b = line.split("~")
        a = tuple(map(int, a.split(",")))
        b = tuple(map(int, b.split(",")))
        res.append((a, b))

    return res


def move_piece_down(piece):
    a, b = piece
    x1, y1, z1 = a
    x2, y2, z2 = b
    return ((x1, y1, z1 - 1), (x2, y2, z2 - 1))


def move_piece_up(piece):
    a, b = piece
    x1, y1, z1 = a
    x2, y2, z2 = b
    return ((x1, y1, z1 + 1), (x2, y2, z2 + 1))


def check_collision(piece, stack):
    a, b = piece
    x1, y1, z1 = a
    x2, y2, z2 = b
    if z1 == 0 or z2 == 0:
        return True
    
    for p in stack:
        c, d = p
        x1_, y1_, z1_ = c
        x2_, y2_, z2_ = d

        x_overlap = x1 <= x2_ and x2 >= x1_
        y_overlap = y1 <= y2_ and y2 >= y1_
        z_overlap = z1 <= z2_ and z2 >= z1_
        if x_overlap and y_overlap and z_overlap:
            return True
    return False


def gen_dep_graph(stack):
    graph = defaultdict(set)
    for i, piece1 in enumerate(stack):
        for piece2 in stack[i+1:]:
            a, b = piece1
            x1, y1, z1 = a
            x2, y2, z2 = b
            
            c, d = piece2
            x1_, y1_, z1_ = c
            x2_, y2_, z2_ = d
            
            z1 += 1
            z2 += 1
            
            x_overlap = x1 <= x2_ and x2 >= x1_
            y_overlap = y1 <= y2_ and y2 >= y1_
            z_overlap = z1 <= z2_ and z2 >= z1_

            if x_overlap and y_overlap and z_overlap:
                graph[piece1].add(piece2)
    return graph


def solve(data):
    data = sorted(data, key=lambda x: x[0][2])
    stack = []
    for i, (a, b) in enumerate(data):
        while not check_collision((a, b), stack):
            a, b = move_piece_down((a, b))
        (a, b) = move_piece_up((a, b))
        stack.append((a, b))

    p1 = 0
    dependencies = gen_dep_graph(stack)
    for i, p in enumerate(stack):
        if p not in dependencies:
            p1 += 1
            continue
    
        sets = set()
        for k in dependencies:
            if k != p:
                sets |= dependencies[k]
        if all(a in sets for a in dependencies[p]):
            p1 += 1
    
    p2 = 0
    for p in stack:
        s = [p]
        visited = set()
        while s:
            curr = s.pop(0)
            sets = set()

            for k in dependencies:
                if k == p: continue
                if k not in visited:
                    sets |= dependencies[k]

            for k in dependencies[curr]:
                if k not in sets:
                    visited.add(k)
                    s.append(k)
        p2 += len(visited)
    return p1, p2


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
