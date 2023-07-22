from unittest import TestCase
from math import inf
from NegativeCycle.detecting_anomalies import negative_cycle, bellman_ford


class Test(TestCase):
    def test_bellman_ford(self):
        data = [5, 7, 1, 2, 4, 1, 3, 3, 2, 3, -2, 2, 4, 4, 3, 4, -3, 3, 5, 1, 4, 5, 2]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(bellman_ford(adj, cost, 0), -1)

    def test_negative_cycle(self):
        data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 1)

    def test_negative_cycle_1(self):
        data = [6, 11, 1, 6, -10, 1, 2, 3, 2, 6, 8, 2, 3, 3, 2, 5, -5, 3, 5, 1, 3, 6, 3, 3, 4, 2, 5, 4, 0, 6, 5, 5, 6, 2, 2]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 0)

    def test_negative_cycle_3(self):
        data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 0)

    def test_negative_cycle_4(self):
        data = [4, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 0)

    def test_negative_cycle_5(self):
        data = [6, 11, 1, 6, -10, 1, 2, 3, 2, 6, 8, 2, 3, 3, 2, 5, -5, 3, 5, 1, 3, 6, 3, 3, 4, 2, 5, 4, 0, 6, 5, 5, 6, 2, 2]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 0)

    def test_negative_cycle_6(self):
        data = [6, 11, 1, 2, -10, 1, 3, 3, 2, 3, 2, 3, 2, 8, 2, 4, 5, 3, 4, -5, 3, 5, 3, 5, 4, 1, 5, 2, 3, 5, 6, 2, 4, 6, 0]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 0)

    def test_negative_cycle_7(self):
        data = [6, 9, 1, 3, 1, 1, 5, 1, 5, 3, 1, 4, 1, 1, 3, 4, 1, 4, 6, 1, 3, 2, -5, 2, 6, 1, 6, 3, 1]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 1)

    def test_negative_cycle_8(self):
        data = [7, 7, 1, 2, -1, 2, 3, -1, 3, 4, -1, 4, 1, 1, 5, 6, 1, 6, 7, 1, 7, 5, 1]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 1)

    def test_negative_cycle_9(self):
        data = [4, 3, 1, 2, -1, 2, 3, -2, 3, 4, -3]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 0)

    def test_negative_cycle_10(self):
        data = [5, 5, 1, 2, 1, 3, 1, 1, 3, 4, -1, 4, 5, -1, 5, 3, -1]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w

        self.assertEqual(negative_cycle(adj, cost), 1)

