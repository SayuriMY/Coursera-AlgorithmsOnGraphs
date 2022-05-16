# Uses python3
"""
File name: connecting_points_kruskal.py
Author: Sayuri Monarrez Yesaki
Date created: 05/15/2022
Date last modified: 05/15/2022
Python version: 3.9

The goal is to build roads between some pairs of the given cities such that there is a path between any two cities
and the total length of the roads is minimized.

Task: Given n points on a plane, connect them with segments of minimum total length such that there is a path between
any two points. Recall that the length of a segment with endpoints (x1, y1 ) and (x2, y2 ) is equal to
( (x1 - x2)^2 + (y1 - y2) ^2 ) ^1/2.

Input: The first line contains the number of n points. Each of the following n lines defines a point (xi, yi).

Constraints: 1 <= n <= 200; -10^3<= xi, yi<= 10^3 are integers; All points are pairwise different, no three points
lie on the same line.

Output: Output the minimum total length of segments. The absolute value of the difference between the answer of your
program and the optimal value should be at most 10^-6. To ensure this, output your answer with at least seven digit
after the decimal point (otherwise your answer, whitle being computed correctly, can turn out to be wrong because of
rounding issues.)

Time limit: 10 sec

Memory Limit: 512 MB
"""

import sys
import math

def minimum_distance(x, y):
    result = 0.
    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))