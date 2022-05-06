#Uses python3
"""
File name: flight_segments.py
Author: Sayuri Monarrez Yesaki
Date created: 04/21/2022
Date last modified: 04/22/2022
Python version: 3.9

You would like to compute the minimum number of flight segments to get from one city to another one. For this,
you construct the following undirected graph: vertices represent cities, there is an edge between two vertices
whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest path from one
of the given cities to the other one.

Task: Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length of a
shortest path between u and v (that is, the minimum number of edges in a path from u to v).

Input: A graph is given in the standard format. The next line contains two vertices u and v.

Constraints: 2 <= n <= 10^5; 0 <= m <= 10^5; u != v, 1 <= u, v <= n.

Output: Output the minimum number of edges in a path from u to v, or -1 if there is no path.

Time limit: 10 sec

Memory Limit: 512 MB
"""

import sys
import queue

def bipartite(adj):
    #write your code here
    return -1

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