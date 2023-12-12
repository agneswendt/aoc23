import time
from aocd.models import Puzzle
from functools import cache
import itertools


day, year = 12, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        line, rules = line.split()
        rules = list(map(int, rules.split(",")))
        res.append((line, rules))
    return res


@cache
def calc(line, rules, curr=0):
    if not line:
        return len(rules) == 0 if not curr else (len(rules) == 1 and rules[0] == curr)

    if (not rules or curr > rules[0]) and curr:
        return 0

    match line[0]:
        case "?":
            if not rules or curr == rules[0]:
                return calc(line[1:], rules[1:], 0)
            if curr:
                return calc(line[1:], rules, curr + 1)
            return calc(line[1:], rules, 0) + calc(line[1:], rules, curr + 1)
        case ".":
            if curr:
                return 0 if rules[0] != curr else calc(line[1:], rules[1:], 0)
            return calc(line[1:], rules, 0)
        case "#":
            return calc(line[1:], rules, curr + 1)


def p1(data):
    res = 0
    for line, rules in data:
        res += calc(line, tuple(rules))
    return res


def p2(data):
    res = 0
    for line, rules in data:
        n_l = "?".join([line] * 5)
        n_r = rules * 5
        res += calc(n_l, tuple(n_r))
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
