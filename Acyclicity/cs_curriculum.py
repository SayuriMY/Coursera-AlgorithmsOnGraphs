# python3
"""
File name: cs_curriculum.py
Author: Sayuri Monarrez Yesaki
Date created: 04/13/2022
Date last modified: 04/13/2022
Python version: 3.9

A computer science curriculum specifies the prerequisites for each course as a list of courses that should be taken
before taking this course. You would like to perform a consistency check of the curriculum, that is, to check that
there are no cyclic dependencies. For this, you construct the following directed graph: vertices correspond to courses,
there is a directed edges (u, v) is the course u should be taken before the course v. Then, it is enough to check
whether the resulting graph contains a cycle.

Task: Check whether a given directed graph with n vertices and m edges contains a cycle.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^3

Output: Output 1 if the graph contains a cycle and 0 otherwise.

Time limit: 5 sec

Memory Limit: 512 MB
"""

import sys


def acyclic(adj):
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
