import time
from aocd.models import Puzzle


day, year = 2, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        l = line.split(': ')[1].split('; ')
        r = []
        for g in l:
            r.append(tuple(g.split(', ')))
        res.append(r)
    return res


def p1(data):
    red = 12
    green = 13
    blue = 14
    possible = set(range(len(data)+1))
    for i, l in enumerate(data):
        for s in l:
            for c in s:
                num, color = c.split(' ')
                num = int(num)
                if color == 'red':
                    if num > red:
                        possible -= {i+1}
                        break
                if color == 'blue':
                    if num > blue:
                        possible -= {i+1}
                        break
                if color == 'green':
                    if num > green:
                        possible -= {i+1}
                        break
    return sum(list(possible))
        


def p2(data):
    res = 0
    for l in data:
        red = 0
        blue = 0
        green = 0
        for s in l:
            for c in s:
                num, color = c.split(' ')
                num = int(num)
                if color == 'red':
                    red = max(num, red)
                if color == 'blue':
                    blue = max(num, blue)
                if color == 'green':
                    green = max(num, green)
        res += red * blue * green
    return res


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
