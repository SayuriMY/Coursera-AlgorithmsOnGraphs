from unittest import TestCase
from math import inf
from ShortestPaths.exchanging_money import shortet_paths


class Test(TestCase):
    def test_shortest_paths_1(self):
        data = [6, 7, 1, 2, 10, 2, 3, 5, 1, 3, 100, 3, 5, 7, 5, 4, 10, 4, 3, -18, 6, 1, -1, 1]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s = data[0]
        s -= 1
        distance = [10 ** 19] * n
        reachable = [0] * n
        shortest = [1] * n

        shortet_paths(adj, cost, s, distance, reachable, shortest)

        self.assertEqual(distance[0], 0)
        self.assertEqual(distance[1], 10)
        self.assertEqual(distance[n - 1], inf)
        self.assertEqual(reachable, [1, 1, 1, 1, 1, 0])
        self.assertEqual(shortest, [1, 1, 0, 0, 0, 1])

    def test_shortest_paths_2(self):
        data = [5, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 3, 1, -5, 4]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s = data[0]
        s -= 1
        distance = [10 ** 19] * n
        reachable = [0] * n
        shortest = [1] * n

        shortet_paths(adj, cost, s, distance, reachable, shortest)

        self.assertEqual(distance[3], 0)
        self.assertEqual(reachable, [1, 1, 1, 1, 0])
        self.assertEqual(shortest, [0, 0, 0, 1, 1])


