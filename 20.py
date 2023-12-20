import time
from aocd.models import Puzzle
from collections import defaultdict
from math import lcm


day, year = 20, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    res = {}
    rev = defaultdict(list)
    for line in data.splitlines():
        name, rest = line.split(" -> ")
        rest = rest.split(", ")
        res[name] = rest
        for r in rest:
            rev[r].append(name)

    return res, dict(rev)


def solve(data):
    p1, p2 = 0, 0
    outputs, inputs = data
    n_map = {}
    for k in outputs:
        if "%" in k or "&" in k:
            n_map[k[1:]] = k
        else:
            n_map[k] = k
    for k in inputs:
        if k not in n_map:
            n_map[k] = k

    state = {}
    highs, lows = 0, 0
    index = 0
    ones = [0, 0, 0, 0]
    while True:
        if index == 1000:
            p1 = lows * highs
        lows += 1
        queue = [("button", "broadcaster", 0)]
        while queue:
            origin, curr, pulse = queue.pop(0)
            if curr == "broadcaster":
                pass
            else:
                s, name = curr[0], curr[1:]
                if s == "%":
                    if pulse == 1:
                        continue
                    else:
                        if name not in state:
                            state[name] = 0
                        if state[name] == 1:
                            state[name] = 0
                            pulse = 0
                        else:
                            state[name] = 1
                            pulse = 1

                elif s == "&":
                    if name not in state:
                        state[name] = []
                        for n2 in inputs[name]:
                            if n2 == origin:
                                state[name].append(pulse)
                            else:
                                state[name].append(0)
                    elif name in state:
                        if origin in inputs[name]:
                            state[name][inputs[name].index(origin)] = pulse
                    if all(state[name]):
                        pulse = 0
                    else:
                        pulse = 1
                    if curr == inputs["rx"][0] and any(state[name]):
                        for i in range(len(ones)):
                            if state[name][i] == 1 and ones[i] == 0:
                                ones[i] = index
                        if all(ones):
                            p2 = lcm(*[x + 1 for x in ones])
                            return p1, p2
                else:
                    continue
            for output in outputs[curr]:
                if pulse == 1:
                    highs += 1
                else:
                    lows += 1
                queue.append((curr, n_map[output], pulse))
        index += 1


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
