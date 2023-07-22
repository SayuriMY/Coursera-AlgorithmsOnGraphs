from unittest import TestCase
from Bipartite.bipartite_graph import bipartite


class Test(TestCase):
    def test_bipartite(self):
        data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        self.assertEqual(bipartite(adj), 1)

    def test_bipartite_1(self):
        data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        self.assertEqual(bipartite(adj), 0)
