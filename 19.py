import time
from aocd.models import Puzzle


day, year = 19, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    workflows = {}
    ratings = []
    used = False
    for line in data.splitlines():
        if not line:
            used = True
            continue
        if used:
            ratings.append([int(i.split("=")[1]) for i in line[1:-1].split(",")])
        else:
            name = line.split("{")[0]
            rules = line.split("{")[1][:-1].split(",")
            res = []
            for rule in rules:
                if "<" in rule or ">" in rule:
                    r = tuple(rule.split(":"))
                else:
                    r = rule
                res.append(r)
            workflows[name] = res
    return (workflows, ratings)


def traverse(workflows, rating, curr="in"):
    if curr == "A":
        return True
    if curr == "R":
        return False
    x, m, a, s = rating
    for rule in workflows[curr]:
        if isinstance(rule, tuple) and (">" or "<" in rule[0]):
            res = eval(rule[0])
            if res:
                return traverse(workflows, rating, curr=rule[1])
        else:
            return traverse(workflows, rating, curr=rule)


def p1(data):
    workflows, ratings = data
    res = 0
    for rating in ratings:
        x, m, a, s = rating
        if traverse(workflows, rating):
            res += x + m + a + s
    return res


def calc(workflows, vars, curr="in", r1=1, r2=4001):
    if curr == "A":
        res = 1
        for x1, x2 in vars:
            res *= x2 - x1
        return res
    if curr == "R":
        return 0
    res = 0
    for rule in workflows[curr]:
        if isinstance(rule, tuple) and (">" or "<" in rule[0]):
            rule, dest = rule
            if "<" in rule:
                num = int(rule.split("<")[1])
                i = "xmas".index(rule[0])
                l, u = vars[i]
                vars[i] = (l, min(u, num))
                res += calc(workflows, vars.copy(), curr=dest)
                vars[i] = (num, min(u, 4001))
            elif ">" in rule:
                num = int(rule.split(">")[1]) + 1
                i = "xmas".index(rule[0])
                l, u = vars[i]
                vars[i] = (max(l, num), u)
                res += calc(workflows, vars.copy(), curr=dest)
                vars[i] = (max(1, l), num)
        else:
            res += calc(workflows, vars, curr=rule)
    return res


def p2(data):
    return calc(data[0], [(1, 4001)] * 4)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
