# python3
"""
File name: cs_curriculum.py
Author: Sayuri Monarrez Yesaki
Date created: 04/15/2022
Date last modified: 04/15/2022
Python version: 3.9

Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to find an
order of all courses that is consistent with all dependencies. For this, you find a topological ordering of the
corresponding directed graph.

Task: Compute a topological ordering of a given directed graph (DAG) with n vertices and m edges.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^5; 0 <= m <= 10^5. The given graph is guaranteed to be acyclic

Output: Output any topological ordering of its vertices

Time limit: 10 sec

Memory Limit: 512 MB
"""
import sys


def dfs(adj, used, order, x):
    # write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # write your code here
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
