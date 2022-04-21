from unittest import TestCase
from Acyclicity.cs_curriculum import acyclic, Graph


class Test(TestCase):
    def test_acyclic(self):
        data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)
        rev_adj = Graph(n, edges, True)

        self.assertEqual(acyclic(adj, rev_adj), 1)

    def test_acyclic_1(self):
        data = [5, 7, 1, 2, 2, 3, 1, 3, 3, 4, 1, 4, 2, 5, 3, 5]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)
        rev_adj = Graph(n, edges, True)

        self.assertEqual(acyclic(adj, rev_adj), 0)
