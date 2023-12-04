import time
from aocd.models import Puzzle
from functools import cache


day, year = 4, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        line = line.split(": ")[1]
        groups = line.split(" | ")

        n1 = list(map(int, filter(lambda x: x.isdigit(), groups[0].split(" "))))
        n2 = list(map(int, filter(lambda x: x.isdigit(), groups[1].split(" "))))
        res.append((set(n1), n2))

    return res


def p1(data):
    res = 0
    for card in data:
        w, mine = card
        points = 0
        for c in mine:
            if c in w:
                points = points*2 if points else 1
        res += points
    return res


def p2(data):
    @cache
    def traverse(i):
        if i == len(data):
            return 0
        res = 0
        w, mine = data[i]
        j = 1
        for c in mine:
            if c in w:
                res += traverse(i + j)
                j += 1
        return 1 + res

    res = 0
    for i in range(len(data)):
        res += traverse(i)
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
