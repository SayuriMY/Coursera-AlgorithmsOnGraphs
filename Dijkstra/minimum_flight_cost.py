# Uses python3
"""
File name: minimum_flight_cost.py
Author: Sayuri Monarrez Yesaki
Date created: 05/06/2022
Date last modified: 05/06/2022
Python version: 3.9

You're interested in minimizing not the number of segments, but the total cost of a flight. For this, you construct
a weighted graph: the weight of an edge from one city to another one is the cost of the corresponding flight.

Task: Given an directed graph with positive edge weights and with n vertices and m edges as well as two vertices
u and v, compute the weight of a shortest path between u and v (that is, the minimum total weight of a path from
u and v).

Input: A graph is given in the standard format. The next line contains two vertices u and v.

Constraints: 1 <= n <= 10^4; 0 <= m <= 10^5, u != v, 1 <= u, v <= n, edge weights are non-negative integers not
exceeding 10^8.

Output: Output the minimum weight of a path from u to v, or -1 if there is no path.

Time limit: 10 sec

Memory Limit: 512 MB
"""
import sys
import queue


def distance(adj, cost, s, t):
    #write your code here
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))