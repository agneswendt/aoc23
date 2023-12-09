import time
from aocd.models import Puzzle


day, year = 9, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        res.append(list(map(int, line.split(" "))))
    return res


def solve(data):
    p1 = 0
    p2 = 0
    for seq in data:
        hist = [seq]
        while any(seq):
            n_seq = []
            for i in range(1, len(seq)):
                n_seq.append(seq[i] - seq[i - 1])
            seq = n_seq
            hist.append(seq)
        hist[-1].append(0)
        hist[-1].insert(0, 0)
        for i in range(len(hist) - 1, 0, -1):
            hist[i - 1].append(hist[i - 1][-1] + hist[i][-1])
            hist[i - 1].insert(0, hist[i - 1][0] - hist[i][0])
        p1 += hist[0][-1]
        p2 += hist[0][0]
    return (p1, p2)


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1, p2 = solve(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
