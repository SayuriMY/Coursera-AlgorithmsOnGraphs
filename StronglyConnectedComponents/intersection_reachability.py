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
from typing import List
sys.setrecursionlimit(200000)


class Graph:
    def __init__(self, n: int, edges: List[tuple], reversed: bool=False):
        """Constructor of the Graph Class

        Parameters
        ----------
        n: int
            Number of vertices in a graph
        edges: List[tuples]
            List of tuples representing the edges in a graph
        reversed: bool
            Flag to state the directed edge should be inverted to create a reversed graph
        """
        self.adj = self._initialize(n, edges, reversed)
        # initialize list of all vertices in the adj graph - mark all as unvisited.
        self.visited = [0] * n
        # initialize list to keep postvisit records on each vertex
        self.postorder = []
        self.scc = [0] * n
        self.scc_num = 1

    def _initialize(self, n: int, edges: List[tuple], reversed: bool) -> List[List[int]]:
        """Initializes the Graph using the adjacency list representation

        Parameters
        ----------
        n: int
            Number of vertices in a graph
        edges: List[tuples]
            List of tuples representing the edges in a graph
        reversed: bool
            Flag to state the directed edge should be inverted to create a reversed graph

        Returns
        -------
        adj: List[List[int]]
            Graph - adjacency list representation
        """
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            if reversed:
                adj[b - 1].append(a - 1)
            else:
                adj[a - 1].append(b - 1)
        return adj

    def is_visited(self, vertex: int) -> bool:
        """Check if the given vertex has been visited.

        Parameters
        ----------
        vertex: int
            int representing the given vertex in the visited array

        Returns
        -------
        bool
            True if the vertex has been visited ( equal to 1), False otherwise.
        """
        return self.visited[vertex] == 1

    def mark_visited(self, vertex: int) -> None:
        """Mark that a given vertex has been visited

        Parameters
        ----------
        vertex: int
            int representing the given vertex in the visited array
        """
        self.visited[vertex] = 1

    def mark_scc(self, vertex: int) -> None:
        """Mark the strongly connected component for a given vertex

        Parameters
        ----------
        vertex: int
           int representing the given vertex in the visited array
        """
        self.scc[vertex] = self.scc_num

    def explore(self, x: int) -> None:
        """Recursively explore nodes reachable from x. Neighbors only marked as visited when
        explored.

        Parameters
        ----------
        x: int
            current vertex
        """

        # mark neighbor vertex as visited
        self.mark_visited(x)

        self.mark_scc(x)

        # explore neighbors
        for neighbor in self.adj[x]:
            # if neighbor is 0 in visited list, it means it has not been visited yet.
            if not self.is_visited(neighbor):
                self.explore(neighbor)

        # post order
        self.postorder.insert(0, x)

    def DFS(self) -> None:
        """Use depth-first search algorithm to explore/traverse the given graph
        """

        for vertex in range(len(self.adj)):
            # if vertex is 0 in visited list, it means it has not been visited yet.
            if not self.is_visited(vertex):
                # explore neighbor vertices reachable from the current vertex
                self.explore(vertex)
                self.scc_num += 1


def number_of_strongly_connected_components(graph: Graph, rev_graph: Graph) -> int:
    """Find the number of strongly connected components in the corresponding graph.

    Parameters
    ----------
    graph: Graph
        Graph object

    rev_graph: Graph
        Graph object representation of the reversed graph

    Returns
    -------
    int
        Number of strongly connected components.
    """

    # DFS on reversed graph recording the post order of each vertex.
    rev_graph.DFS()

    for v in rev_graph.postorder:
        if not graph.is_visited(v):
            graph.explore(v)
            graph.scc_num += 1

    return graph.scc_num - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = Graph(n, edges)
    rev_adj = Graph(n, edges, True)

    print(number_of_strongly_connected_components(adj, rev_adj))
