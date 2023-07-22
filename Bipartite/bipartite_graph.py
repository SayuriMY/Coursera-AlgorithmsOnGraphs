# Uses python3
"""
File name: bipartile_graph.py
Author: Sayuri Monarrez Yesaki
Date created: 04/21/2022
Date last modified: 04/25/2022
Python version: 3.9

An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the graph
joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph is used to
model connections between objects of two different types (say, boys and girls; or students and dormitories).

An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
(say, black and white) such that the endpoints of each edge have different colors.

Task: Given an undirected graph with n vertices and m edges, check whether it is bipartite.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^5; 0 <= m <= 10^5

Output: Output 1 if the graph is bipartite, 0 otherwise.

Time limit: 10 sec

Memory Limit: 512 MB
"""

import sys
from typing import List, Union


def bfs(adj: List[List[int]], s: int, assigned_color: List[Union[None, int]]):
    """Use Bread-First Search to explore/traverse the given graph

    Parameters
    ----------
    adj: List[List[int]]
            Graph - adjacency list representation
    s: int
        origin neighbor

    assigned_color: List[float]
        array of the distance between origin s to each other neighbor. - 0 --> white; 1 --> black
    """

    assigned_color[s] = 0

    q = [s]
    while len(q) != 0:
        # dequeue the first element in the queue
        u = q.pop(0)

        # find the
        for neighbor in adj[u]:
            if assigned_color[neighbor] is None:
                q.append(neighbor)

                if assigned_color[u] == 0:
                    assigned_color[neighbor] = 1
                else:
                    assigned_color[neighbor] = 0


def bipartite(adj: List[List[int]]) -> int:
    """Recursively explore nodes reachable from x. Neighbors only marked as visited when
    explored.

    Parameters
    ----------
    adj: List[List[int]]
        Adjacency list representation of graph.
    """

    n = len(adj)

    # array to store the distance between origin, s, to each neighbor
    assigned_color = [None] * n

    for vertex in range(n):
        if assigned_color[vertex] is None:
            bfs(adj, vertex, assigned_color)

    for vertex in range(n):
        for neigh in adj[vertex]:
            if assigned_color[vertex] == assigned_color[neigh]:
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
