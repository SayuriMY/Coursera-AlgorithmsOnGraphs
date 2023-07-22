from unittest import TestCase
from MinimumSpanningTrees.connecting_points_prim import minimum_distance


class Test(TestCase):
    def test_minimum_distance(self):
        data = [4, 0, 0, 0, 1, 1, 0, 1, 1]
        n = data[0]
        x = data[1::2]
        y = data[2::2]
        result = "{0:.9f}".format(minimum_distance(x, y))
        self.assertEqual(result, 3.000000000)

    def test_minimum_distance_1(self):
        data = [5, 0, 0, 0, 2, 1, 1, 3, 0, 3, 2]
        n = data[0]
        x = data[1::2]
        y = data[2::2]
        result = "{0:.9f}".format(minimum_distance(x, y))
        self.assertEqual(result, 7.064495102)
