import time
from aocd.models import Puzzle
import re


day, year = 1, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def p1(data):
    res = 0
    for line in data:
        digit = ""
        for c in line:
            if c.isdigit():
                digit += c
                break
        for c in reversed(line):
            if c.isdigit():
                digit += c
                break
        res += int(digit)
    return res


def p2(data):
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    res = 0
    for line in data:
        min_i = float("inf")
        min_digit = ""
        max_i = -1
        max_digit = ""
        for digit in digits:
            i = [m.start() for m in re.finditer(digit, line)]
            if not i:
                continue
            i1 = i[0]
            i2 = i[-1]
            if i1 < min_i and i1 != -1:
                min_i = i1
                min_digit = digits[digit]
            if i2 > max_i:
                max_i = i2
                max_digit = digits[digit]
        res += int(min_digit + max_digit)
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print(p1, p2)
    print("Time: ", time.time() - start)
