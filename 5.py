import time
from aocd.models import Puzzle


day, year = 5, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    seeds = ""
    res = {}
    curr = ""
    order = []
    for line in data.splitlines():
        if "seeds:" in line:
            seeds = list(map(int, line.split(": ")[1].split(" ")))
        elif not line:
            curr = ""
        elif ":" in line:
            curr = line.split(":")[0].split(" ")[0]
            res[curr] = []
            order.append(curr)
        else:
            res[curr].append(list(map(int, line.split(" "))))
    return (seeds, order, res)


def apply_rules(rule, seeds):
    n_seeds = []
    for seed in seeds:
        for r in rule:
            if r[1] <= seed < r[2] + r[1]:
                b = r[2] + r[1] - seed
                n_seeds.append(seed + (r[0] - r[1]))
                break
        else:
            n_seeds.append(seed)
    return n_seeds


def p1(data):
    seeds, order, rules = data

    for ruleset in order:
        seeds = apply_rules(rules[ruleset], seeds)

    return min(seeds)


def get_min(rules, order, span):
    spans = [span]
    for rule_set in order:
        n_span = []
        for span in spans:
            left, right = span
            changed = False
            for rule in rules[rule_set]:
                dest, source, r = rule
                rule_left, rule_right = (source, source + r)
                if right <= rule_left or left >= rule_right:
                    continue
                else:
                    if left < rule_left:
                        spans.append((left, rule_left))

                    n_span.append(
                        (
                            max(left, rule_left) + (dest - source),
                            min(right, rule_right) + (dest - source),
                        )
                    )

                    if rule_right < right:
                        spans.append((rule_right, right))
                    changed = True
            if not changed:
                n_span.append(span)

        spans = n_span
    return spans


def p2(data):
    seeds, order, rules = data
    first = None
    res = float("inf")
    first = None
    for seed in seeds:
        if not first:
            first = seed
            continue
        else:
            res = min(
                res,
                min(
                    get_min(rules, order, (first, first + seed)),
                    key=lambda x: x[0],
                )[0],
            )
            first = None
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
