from unittest import TestCase
from StronglyConnectedComponents.intersection_reachability import Graph, number_of_strongly_connected_components


class Test(TestCase):
    def test_number_of_strongly_connected_components(self):
        data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)
        rev_adj = Graph(n, edges, True)

        self.assertEqual(number_of_strongly_connected_components(adj, rev_adj), 2)

    def test_number_of_strongly_connected_components_1(self):
        data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
        # get number of vertices n, and number of edges m
        n, m = data[0:2]
        data = data[2:]
        # list of edges - list of tuples that represent edges
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = Graph(n, edges)
        rev_adj = Graph(n, edges, True)

        self.assertEqual(number_of_strongly_connected_components(adj, rev_adj), 5)