from unittest import TestCase
from math import inf
from Dijkstra.minimum_flight_cost import distance, Vertex, MinHeap


class Test(TestCase):
    def test_Vertex_update_distance(self):
        v = Vertex(0, 1)
        self.assertEqual(v.dist, 1)
        v.update_dist(3)
        self.assertEqual(v.dist, 3)

    def test_MinHeap(self):
        dist = [0, inf, inf, 1]
        heap = MinHeap(dist)

        self.assertEqual(heap.size, len(dist))

        expected_dist = [0, 1, inf, inf]
        expected_id = [0, 3, 2, 1]
        for i in range(len(heap.min_heap)):
            vertex = heap.min_heap[i]
            self.assertEqual(vertex.dist, expected_dist[i])
            self.assertEqual(vertex.id, expected_id[i])

    def test_MinHeap_1(self):
        dist = [inf, inf, inf, inf, 0, 4]
        heap = MinHeap(dist)

        self.assertEqual(heap.size, len(dist))

        expected_dist = [0, inf, 4, inf, inf, inf]
        expected_id = [4, 0, 5, 3, 1, 2]
        for i in range(len(heap.min_heap)):
            vertex = heap.min_heap[i]
            self.assertEqual(vertex.dist, expected_dist[i])
            self.assertEqual(vertex.id, expected_id[i])

    def test_distance(self):
        data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), 3)

    def test_distance_1(self):
        data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), 6)

    def test_distance_2(self):
        data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), -1)

    def test_distance_3(self):
        data = [1, 0, 1, 1]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), 0)

    def test_distance_4(self):
        data = [4, 3, 1, 2, 1, 2, 3, 2, 1, 3, 5, 4, 3]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), -1)

    def test_distance_5(self):
        data = [4, 3, 1, 2, 1, 2, 3, 2, 1, 3, 5, 3, 4]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), -1)

    def test_distance_6(self):
        data = [3, 2, 1, 2, 1, 2, 3, 2, 2, 3]
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
        data = data[3 * m:]
        adj = [[] for _ in range(n)]
        cost = [[0] * n for _ in range(n)]
        for ((a, b), w) in edges:
            adj[a - 1].append(b - 1)
            cost[a - 1][b - 1] = w
        s, t = data[0] - 1, data[1] - 1

        self.assertEqual(distance(adj, cost, s, t), 2)
