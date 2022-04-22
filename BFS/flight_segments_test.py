from unittest import TestCase
from BFS.flight_segments import distance


class Test(TestCase):
    def test_distance(self):
        data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        # create graph - adjacency list representation
        x, y = data[2 * m:]
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        s, t = data[2 * m] - 1, data[2 * m + 1] - 1

        self.assertEqual(distance(adj, s, t), 2)

    def test_distance_1(self):
        data = [5, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 5]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        # create graph - adjacency list representation
        x, y = data[2 * m:]
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        s, t = data[2 * m] - 1, data[2 * m + 1] - 1

        self.assertEqual(distance(adj, s, t), -1)