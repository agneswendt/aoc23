import time
from aocd.models import Puzzle


day, year = 3, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(line)
    return res


def p1(data):
    res = 0
    for x, line in enumerate(data):
        curr_digit = ""
        adjacent = False
        for i, c in enumerate(line):
            if data[x][i].isdigit():
                curr_digit += c
                for p in range(max(x - 1, 0), min(x + 2, len(data))):
                    for q in range(max(i - 1, 0), min(i + 2, len(line))):
                        if data[p][q] != "." and not data[p][q].isdigit():
                            adjacent = True
            else:
                if curr_digit and adjacent:
                    res += int(curr_digit)
                curr_digit = ""
                adjacent = False
        if curr_digit and adjacent:
            res += int(curr_digit)

    return res


def find_num(data, x, y):
    num = ""
    for j in range(y, len(data[0])):
        if data[x][j].isdigit():
            num += data[x][j]
        else:
            break
    for j in range(y - 1, -1, -1):
        if data[x][j].isdigit():
            num = data[x][j] + num
        else:
            break
    return num


def find_adjacent(data, x, y):
    chars = []
    for i in range(max(x - 1, 0), min(x + 2, len(data))):
        for j in range(max(y - 1, 0), min(y + 2, len(data[0]))):
            if data[i][j].isdigit():
                chars.append(find_num(data, i, j))
    return chars


def p2(data):
    res = 0
    for x, line in enumerate(data):
        for i, c in enumerate(line):
            if c == "*":
                nums = find_adjacent(data, x, i)
                nums = list(set(nums))
                if len(nums) == 2:
                    res += int(nums[0]) * int(nums[1])
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
