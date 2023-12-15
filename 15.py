import time
from aocd.models import Puzzle


day, year = 15, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line.split(","))
    return res[0]


def get_hash(word):
    curr = 0
    for c in word:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr


def p1(data):
    return sum(get_hash(word) for word in data)


def p2(data):
    boxes = [dict() for _ in range(256)]
    for word in data:
        if "-" in word:
            label = word.split("-")[0]
            box = get_hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        elif "=" in word:
            label, value = word.split("=")
            box = get_hash(label)
            boxes[box][label] = value

    res = 0
    for i, box in enumerate(boxes):
        for j, label in enumerate(box):
            res += int(box[label]) * (i + 1) * (j + 1)
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
