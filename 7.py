import time
from aocd.models import Puzzle
from functools import cmp_to_key


day, year = 7, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        first, sec = line.split(" ")
        res.append((first, int(sec)))
    return res


def count_chars(hand):
    res = []
    Js = hand.count("J")
    hand = hand.replace("J", "")
    if not hand:
        return [5]
    most_common = max(hand, key=hand.count)
    hand += Js * most_common
    for c in set(hand):
        if c != "J":
            res.append(hand.count(c))
    return list(sorted(res))


def get_rank(count):
    counts = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 2, 2],
        [1, 1, 3],
        [2, 3],
        [1, 4],
        [5],
    ]
    return counts.index(count)


def comparator(a, b):
    a, b = a[0], b[0]
    sorting = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    order = {v: i for i, v in enumerate(sorting)}
    for a, b in zip(a, b):
        if order[a] > order[b]:
            return 1
        elif order[a] < order[b]:
            return -1


def p2(data):
    cards = [[], [], [], [], [], [], []]
    for hand, card in data:
        count = count_chars(hand)
        type = get_rank(count)
        cards[type].append((hand, card))

    cmp = cmp_to_key(comparator)
    rank = []
    for lst in cards:
        for elem in reversed(sorted(lst, key=cmp)):
            rank.append(elem[1])
    res = 0
    for i, j in enumerate(rank):
        res += (i + 1) * j
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    # p1 = p1(data)
    p2 = p2(data)
    # print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
