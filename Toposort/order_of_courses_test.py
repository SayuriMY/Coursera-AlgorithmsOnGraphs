from unittest import TestCase
from Toposort.order_of_courses import Graph


class TestGraph(TestCase):
    def test_toposort(self):
        data = [4, 3, 1, 2, 4, 1, 3, 1]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)

        self.assertEqual(adj.toposort(), [3, 2, 0, 1])

    def test_toposort_1(self):
        data = [4, 1, 3, 1]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)

        self.assertEqual(adj.toposort(), [3, 2, 1, 0])

    def test_toposort_2(self):
        data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)

        self.assertEqual(adj.toposort(), [4, 3, 2, 1, 0])