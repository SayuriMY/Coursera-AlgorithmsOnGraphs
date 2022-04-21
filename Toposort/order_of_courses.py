# python3
"""
File name: order_of_courses.py
Author: Sayuri Monarrez Yesaki
Date created: 04/15/2022
Date last modified: 04/15/2022
Python version: 3.9

Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to find an
order of all courses that is consistent with all dependencies. For this, you find a topological ordering of the
corresponding directed graph.

Task: Compute a topological ordering of a given directed graph (DAG) with n vertices and m edges.

Input: A graph is given in the standard format.

Constraints: 1 <= n <= 10^5; 0 <= m <= 10^5. The given graph is guaranteed to be acyclic

Output: Output any topological ordering of its vertices

Time limit: 10 sec

Memory Limit: 512 MB
"""
import sys
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[tuple]):
        """Constructor of the Graph Class

        Parameters
        ----------
        n: int
           Number of vertices in a graph
        edges: List[tuples]
           List of tuples representing the edges in a graph
        """

        self.adj = self._initialize(n, edges)
        # initialize list of all vertices in the adj graph - mark all as unvisited.
        self.visited = [0] * n
        # initialize list to keep postvisit records on each vertex
        self.postorder = []
        self.clock = 1

    def _initialize(self, n: int, edges: List[tuple]) -> List[List[int]]:
        """Initializes the Graph using the adjacency list representation

        Parameters
        ----------
        n: int
            Number of vertices in a graph
        edges: List[tuples]
            List of tuples representing the edges in a graph

        Returns
        -------
        adj: List[List[int]]
            Graph - adjacency list representation
        """

        adj = [[] for _ in range(n)]
        for (a, b) in edges:
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

        # explore neighbors
        for neighbor in self.adj[x]:
            # if neighbor is 0 in visited list, it means it has not been visited yet.
            if not self.is_visited(neighbor):
                self.explore(neighbor)

        # post order
        self.postorder.insert(0, x)

    def dfs(self) -> None:
        """Use depth-first search algorithm to explore/traverse the given graph
        """

        for vertex in range(len(self.adj)):
            # if vertex is 0 in visited list, it means it has not been visited yet.
            if not self.is_visited(vertex):
                # explore neighbor vertices reachable from the current vertex
                self.explore(vertex)

    def toposort(self) -> List[int]:
        """Use depth-first search to traverse a graph and get the linear ordering of its vertices.

        Returns
        ----------
        List[int]
            linear order of vertices in the graph.
        """
        # run depth first search on graph
        self.dfs()

        return self.postorder


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = Graph(n, edges)

    order = adj.toposort()
    for x in order:
        print(x + 1, end=' ')
