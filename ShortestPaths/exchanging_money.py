# Uses python3
"""
File name: exchanging_money.py
Author: Sayuri Monarrez Yesaki
Date created: 05/10/2022
Date last modified: 05/11/2022
Python version: 3.9

Compute an optimal way of exchanging the given currency ci into all other currencies. For this, you find shortest
paths from the vertex ci to all the other vertices.

Task: Given a directed graph with possibly negative edge weights and with n vertices and m edges as well as its
vertex s, compute the length of shortest paths from s to all other vertices of the graph.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^4, 1 <= s <= n, edge weights are integers of absolute value of at most 10 ^9.

Output: For all vertices i from 1 to n output the following on a separate line:
    => "*", if there is no path from s to n
    => "-", if there is a path from s to u, but there is no shortest path from s to u (that is, the distance from s to
            u is -inf ).
    => the length of a shortest path otherwise.

Time limit: 10 sec

Memory Limit: 512 MB
"""
import sys
from math import inf
from typing import List, Union


def bellman_ford(adj: List[List[int]], cost: List[List[int]], s: int, shortest: List[int], distan: List[Union[float, int]]) -> List[Union[float,int]]:
    n = len(adj)

    dist = [inf] * n
    prev = [-1] * n

    dist[s] = 0
    last_node_relaxed = -1

    # repeat |V| - 1 times.
    for iter in range(n):
        last_node_relaxed = -1

        for vertex in range(n):
            for neigh in adj[vertex]:
                if distan[neigh] > distan[vertex] + cost[vertex][neigh]:
                    distan[neigh] = distan[vertex] + cost[vertex][neigh]

                # relax
                if dist[neigh] > dist[vertex] + cost[vertex][neigh]:
                    dist[neigh] = dist[vertex] + cost[vertex][neigh]
                    prev[neigh] = vertex

                    last_node_relaxed = neigh

                    if iter == n - 1:
                        shortest[neigh] = 0

        # stop iterations if distance cannot be further improved.
        if last_node_relaxed == -1:
            break

    return dist


def shortet_paths(adj, cost, s, distance, reachable, shortest):

    distan = [inf] * len(adj)
    distan[s] = 0

    for iter in range(len(adj)):
        dist = bellman_ford(adj, cost, iter, shortest, distan)

        # if iter == s:
        #     for i in range(len(adj)):
        #         # if i is s, then it is reachable
        #         if dist[i] != inf:
        #             reachable[i] = 1
        #
        #         distance[i] = dist[i]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[0] * n for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1][b - 1] = w
    s = data[0]
    s -= 1
    distance = [10 ** 19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
