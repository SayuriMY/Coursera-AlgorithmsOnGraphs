# python3
"""
File name: intersection_reachability.py
Author: Sayuri Monarrez Yesaki
Date created: 04/15/2022
Date last modified: 04/15/2022
Python version: 3.9

The police department of a city has made all streets one-way. You would like to check whether it is still possible
to drive legally from any intersection to any other intersection. For this, you construct a directed graph: vertices
are intersections, there is an edge (u, v) whenever there is a (one-way) street from u to v in the city. Then, it
suffices to check whether all the vertices in the graph lie in the same strongly connected component.

Task: Compute the number of strongly connected components of a given directed graph with n vertices and m edges.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^4; 0 <= m <= 10^4.

Output: Output the number of strongly connected components.

Time limit: 5 sec

Memory Limit: 512 MB
"""
import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0
    # write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
