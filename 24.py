import time
from aocd.models import Puzzle
from itertools import combinations
import numpy as np
import itertools


day, year = 24, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    for line in data.splitlines():
        pos, vel = line.split(" @ ")
        pos = tuple(map(int, pos.split(",")))
        vel = tuple(map(int, vel.split(",")))
        res.append((pos, vel))
    return res


def p1(data):
    scope = (200000000000000, 400000000000000)
    res = 0
    for (pos1, vel1), (pos2, vel2) in combinations(data, 2):
        (x1, y1, _), (x2, y2, _)  = pos1, vel1
        (x3, y3, _), (x4, y4, _)  = pos2, vel2
        
        a = ((y1 + y2) - y1) / ((x1 + x2) - x1)
        b = ((y3 + y4) - y3) / ((x3 + x4) - x3)
        
        if a == b:
            continue
        
        c = y1 - a * x1
        d = y3 - b * x3
        
        x, y = ((d - c) / (a - b)), (a * (d-c) / (a - b) + c)
        
        if scope[0] <= x <= scope[1] and scope[0] <= y <= scope[1]:
            x_a = (y - c) / a
            x_b = (y - d) / b
            
            if x2 < 0 and x_a > x1:
                continue
            if x4 < 0 and x_b > x3:
                continue
            if x2 > 0 and x_a < x1:
                continue
            if x4 > 0 and x_b < x3:
                continue
            res += 1
    return res


def p2(data):
    M = []
    sols = []
    for (pos1, vel1), (pos2, vel2) in itertools.pairwise(data):
        x1, y1, _ = pos1
        x2, y2, _ = pos2
        
        dx1, dy1, _ = vel1
        dx2, dy2, _ = vel2
        
        j1 =  (dy2 - dy1)
        j2 = (dx1 - dx2)
        j3 = (y1 - y2)
        j4 = (x2 - x1)
        
        sol = (dx1 * y1 - dx2 * y2 + x2 * dy2 - x1 * dy1)
        M.append((j1, j2, j3, j4))
        sols.append(sol)
        if len(M) == 4:
            break
    M = np.array(M)
    sols = np.array(sols)
    
    x = np.linalg.inv(M) @ sols
    a, b, d, _ = x
    pos1, vel1 = data[0]
    pos2, vel2 = data[1]
    
    time1 = (a - pos1[0]) / (vel1[0] - d)
    time2 = (a - pos2[0]) / (vel2[0] - d)
    
    exp = ((pos1[2] - pos2[2]) + time1 * vel1[2] - time2*vel2[2]) / (time1 - time2)
    c = pos1[2] + time1 * (vel1[2] - exp)
    return a + b + c


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    p1 = p1(data)
    p2 = p2(data)
    print("Part 1: ", p1)
    print("Part 2: ", p2)
    print("Time: ", time.time() - start)
