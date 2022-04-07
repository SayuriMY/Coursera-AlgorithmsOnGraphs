from unittest import TestCase
from ConnectedComponents.adding_exit_to_maze import number_of_components


class Test(TestCase):
    def test_number_of_components(self):
        data = [4, 2, 1, 2, 3, 2]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        # create graph - adjacency list representation
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        self.assertEqual(number_of_components(adj), 2)

    def test_number_of_components_1(self):
        data = [1, 0]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        # create graph - adjacency list representation
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        self.assertEqual(number_of_components(adj), 1)

    def test_number_of_components_2(self):
        data = [4, 0]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        # create graph - adjacency list representation
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        self.assertEqual(number_of_components(adj), 4)
