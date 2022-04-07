# python3
"""
File name: adding_exit_to_maze.py
Author: Sayuri Monarrez Yesaki
Date created: 04/07/2022
Date last modified: 04/07/2022
Python version: 3.9

A maze is a rectangular grid of cells with walls between some of adjacent cells. The maze is represented as an
undirected graph: vertices of the graph are cells of the maze, two vertices are connected by an undirected edge if
they are adjacent and there is no wall between them. You would like to check there are no dead zones in a maze,
that is, that at least one exit is reachable from each cell. For this, you find connected components of the
corresponding undirected graph and ensure that each component contains an exit cell.

Task: Given an undirected graph with n vertices and m edges, compute the number of connected components in it.

Input: An undirected graph with n vertices and m edges.

Constraints: 1 <= n <= 10^3; 0 <= m <= 10^3

Output: Output the number of connected components

Time limit: 5 sec

Memory Limit: 512 MB
"""

import sys
from typing import List


def explore(adj: List[List[int]], x: int, visited: List[int], connected_components: List[int], ccnum: int) -> None:
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
    connected_components: List[int]
        list to assign each vertex a number representing the connected component it belongs to.
    ccnum: int
        number representing the connected component
    """

    # mark neighbor vertex as visited
    visited[x] = 1
    # assign the vertex a number representing the connected component.
    connected_components[x] = ccnum
    # explore neighbors
    for neighbor in adj[x]:
        # if neighbor is 0 in visited list, it means it has not been visited yet.
        if visited[neighbor] == 0:
            explore(adj, neighbor, visited, connected_components, ccnum)


def number_of_components(adj: List[List[int]]) -> int:
    """Find the number of connected components of the corresponding undirected graph

    Parameters
    ----------
    adj: List[List[int]]
        Adjacency list representation of an undirected graph.

    Returns
    -------
    int
        number of connected components.
    """

    # initialize list of all vertices in the adj graph - mark all as unvisited.
    visited = [0] * len(adj)
    # initialize list of the connected component that each vertex belongs to
    connected_components = [0] * len(adj)
    ccnum = 1
    for vertex in range(len(adj)):
        # if vertex is 0 in visited list, it means it has not been visited yet.
        if visited[vertex] == 0:
            # explore neighbor vertices reachable from the current vertex
            explore(adj, vertex, visited, connected_components, ccnum)
            ccnum += 1

    return ccnum - 1


def run_add_exit_to_maze():
    """Main method to find the number of connected components in a graph. Reads input
    from the user - list of numbers separated by spaces representing an
    undirected graph with n vertices and m edges.

        Example: 4 2 1 2 3 2
         n - 4 vertices
         m - 2 edges

         list of edges:
         1 2
         3 2


    After reading the user's input, the graph is constructed using the
    adjacency list representation.
    Prints out the number of connected components
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
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))


if __name__ == '__main__':
    run_add_exit_to_maze()