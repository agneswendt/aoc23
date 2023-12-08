import time
from aocd.models import Puzzle
from itertools import cycle
from functools import cache
from math import lcm


day, year = 8, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res =  {}
    instr = ""
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        if '=' in line:
            name, val = line.split(" = ")
            res[name] = tuple(val[1:-1].split(", "))
        elif line:
            instr += line
    return (instr, res)


def p1(data):
    instr, data = data
    curr = "AAA"
    iter = cycle(instr)
    res = 0
    while curr != "ZZZ":
        res += 1
        instr = next(iter)
        curr = data[curr][0] if instr == "L" else data[curr][1]
    return res


def find_sol(path, data, node):
    i = 0
    while True:
        step = path[i%len(path)]
        node = data[node][0] if step == "L" else data[node][1]
        i+=1
        if node[-1] == "Z":
            return i


def p2(data):
    instr, data = data
    ends = []
    for s in data:
        if s[-1] == "A":
            ends.append(find_sol(instr, data, s))
    return lcm(*ends)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
