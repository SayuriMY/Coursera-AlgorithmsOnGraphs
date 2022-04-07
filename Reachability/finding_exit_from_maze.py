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
from typing import List


def explore(adj: List[List[int]], x: int, visited: List[int]) -> None:
    """Recursively explore nodes reachable from x. Neighbors only marked as visited when
    explored.

    Parameters
    ----------
    adj: List[List[int]]
        Adjacency list representation of graph.
    x: int
        current vertex
    visited: List[int]
        list to keep track of visited vertices ---> 1- visited; 0- not visited
    """

    # mark neighbor vertex as visited
    visited[x] = 1
    # explore neighbors
    for neighbor in adj[x]:
        # if neighbor is 0 in visited list, it means it has not been visited yet.
        if visited[neighbor] == 0:
            explore(adj, neighbor, visited)


def reach(adj: List[List[int]], x: int, y: int) -> int:
    """Check if there is a path between vertices x and y of the adj undirected graph.

    Parameters
    ----------
    adj: List[List[int]]
        Adjacency list representation of an undirected graph.
    x: int
        starting vertex
    y: int
        end vertex

    Returns
    -------
    int
        0 if there is NO path between x and y, 1 otherwise.
    """

    # initialize list of all vertices in the adj graph - mark all as unvisited.
    visited = [0] * len(adj)
    # explore neighbor vertices reachable from x
    explore(adj, x, visited)
    return visited[y]


def run_find_exit_from_maze():
    """Main method to find if there is an exit from a maze. Reads input
    from the user - list of numbers separated by spaces representing an
    undirected graph with n vertices and m edges, and two vertices
    representing the start and end of the maze.

        Example: 3 2 1 2 1 3 2 3
         n - 3 vertices
         m - 2 edges

         list of edges:
         1 2
         1 3

         start maze: 2
         end maze: 3

    After reading the user's input, the graph is constructed using the
    adjacency list representation.
    Prints out 0 if there is NO path between start and end of the maze, 1 otherwise.
    """
    # read input from user
    input = sys.stdin.read()
    # convert input into a list of int
    data = list(map(int, input.split()))
    # get number of vertices n, and number of edges m
    n, m = data[0:2]
    # list of edges
    data = data[2:]
    # list of edges - list of tuples that represent edges
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # create graph - adjacency list representation
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


if __name__ == '__main__':
    run_find_exit_from_maze()
