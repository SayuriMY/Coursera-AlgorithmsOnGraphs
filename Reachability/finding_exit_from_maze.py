# python3
"""
File name: finding_exit_from_maze.py
Author: Sayuri Monarrez Yesaki
Date created: 04/06/2022
Date last modified: 04/06/2022
Python version: 3.9

A maze is a rectangular grid of cells with walls between some of adjacent cells. You would like to check whether
there is a path from a given cell to a given exit from a maze where an exit is also a cell that lies on the border of
the maze. For this, you represent the maze as an undirected graph: vertices of the graph are cells of the maze,
two vertices are connected by an undirected edge if they are adjacent and there is no wall between them. Then, to check
whether there is a path between two given cells in the maze, it suffices to check that there is a path between the
corresponding two vertices in the graph.

Task: Given an undirected graph and two distinct vertices u and v, check if there is a path between u and v.

Input: An undirected graph with n vertices and m edges. The next line contains two vertices u and v of the graph.

Constraints: 2 <= n <= 10^3; 1 <= m <= 10^3; 1 <= u, v <= n; u != n

Output: Output 1 if there is a path between u and v and 0 otherwise.

Time limit: 5 sec

Memory Limit: 512 MB
"""

import sys


def reach(adj, x, y):
    # write your code here
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
