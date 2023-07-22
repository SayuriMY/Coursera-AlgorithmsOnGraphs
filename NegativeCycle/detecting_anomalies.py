# Uses python3
"""
File name: minimum_flight_cost.py
Author: Sayuri Monarrez Yesaki
Date created: 05/08/2022
Date last modified: 05/10/2022
Python version: 3.9

You're given a list of currencies together with a list of exchange rates: rij is the number of units of currency cj
that one gets for one unit of ci. You would like to check whether it is possible to start with one unit of some
currency, perform a sequence of exchanges, and get more than one unit of the same currency. In other words, you
would like to find currencies such that rates > 1. For this, you construct the following graph: vertices are
currencies, the weight of an edge from ci to cj is equal to -log rij. There it suffices to check whether is a
negative cycle in this graph. Indeed, assume that a cycle ci --> cj --> ck --> ci has negative weight. This means
that -(log cij + log cjk + log cki) < 0 and hence log cij + log cjk + log cki > 0

Task: Given a directed graph with possibly negative edge weights and with n vertices and m edges, check whether
it contains a cycle of negative weight.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^4, edge weights are integers of absolute value of at most 10 ^3.

Output: Output 1 if the graph contains a cycle of negative weight and 0 otherwise.

Time limit: 10 sec

Memory Limit: 512 MB
"""
import sys
from math import inf
from typing import List, Union


def bellman_ford(adj: List[List[int]], cost: List[List[int]], s: int) -> int:
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
                # relax
                if dist[neigh] > dist[vertex] + cost[vertex][neigh]:
                    dist[neigh] = dist[vertex] + cost[vertex][neigh]
                    prev[neigh] = vertex

                    last_node_relaxed = neigh

        # stop iterations if distance cannot be further improved.
        if last_node_relaxed == -1:
            break

    return last_node_relaxed


def negative_cycle(adj: List[List[int]], cost: List[List[int]]):
    last_node_relaxed = -1

    for iter in range(len(adj)):
        last_node_relaxed = bellman_ford(adj, cost, iter)

        if last_node_relaxed != -1:
            break

    # Output 1 if the graph contains a cycle of negative weight and 0 otherwise.
    if last_node_relaxed == -1:
        return 0
    return 1


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
    print(negative_cycle(adj, cost))
