import time
from aocd.models import Puzzle
from collections import defaultdict
import numpy as np


day, year = 25, 2023


def get_input():
    puzzle = Puzzle(year, day)
    res = []
    data = """"""
    data = puzzle.input_data
    graph = defaultdict(set)
    for line in data.splitlines():
        name, con = line.split(": ")
        con = con.split(" ")
        for n in con:
            graph[name].add(n)
            graph[n].add(name)

    return graph


def solve(data):
    # https://en.wikipedia.org/wiki/Laplacian_matrix
    indexes = list(data.keys())
        
    A = [[0 for _ in range(len(indexes))] for _ in range(len(indexes))]
    
    for i, n in enumerate(indexes):
        for j, m in enumerate(indexes):
            if n == m:
                continue
            if n in data[m]:
                A[i][j] = 1
                A[j][i] = 1
                
    
    D = [0 for _ in range(len(indexes))]
    
    for i, n in enumerate(indexes):
        for j, m in enumerate(indexes):
            if A[i][j] == 1:
                D[i] += 1
                
    A = np.array(A)
    D = np.diag(np.array(D))
    L = D - A
    eig = np.linalg.eig(L)
    eig_sort = np.argsort(eig.eigenvalues)
    eigenvectors = eig.eigenvectors.T[eig_sort]
    fiedler = eigenvectors[1]

    a = sum(1 if elem > 0 else 0 for elem in fiedler)
    b = sum(1 if elem < 0 else 0 for elem in fiedler)
    return a * b


if __name__ == "__main__":
    start = time.time()
    data = get_input()
    res = solve(data)
    print("Part 1: ", res)
    print("Time: ", time.time() - start)
