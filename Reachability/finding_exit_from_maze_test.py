from unittest import TestCase
from Reachability.finding_exit_from_maze import reach


class Test(TestCase):
    def test_reach(self):
        data = [4, 4, 1, 2, 3, 2, 4, 3, 1, 4, 1, 4]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
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

        self.assertEqual(reach(adj, x, y), 1)

    def test_reach_1(self):
        data = [4, 2, 1, 2, 3, 2, 1, 4]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
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

        self.assertEqual(reach(adj, x, y), 0)