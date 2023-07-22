# Uses python3
"""
File name: connecting_points_prim.py
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
from math import inf, sqrt
from typing import List, Union


class Vertex:
    def __init__(self, vertex_id: int, distance: Union[int, float]):
        """
        Constructor of the Vertex class.

        Parameters
        ----------
        vertex_id: int
            Vertex id.

        distance: int
            Distance from origin node

        """

        self.id = vertex_id
        self.dist = distance

    def update_dist(self, new_dist: Union[int, float]) -> None:
        """
        Update distance from origin node

        Parameters
        ----------
        new_dist: int
            Updated distance
        """

        self.dist = new_dist


class MinHeap:
    def __init__(self, dist: List[Union[int, float]]):
        """
        Constructor of the MinHeap class.

        Parameters
        ----------
        dist: List[int]
            List of the distance of each vertex from origin. This will determine the priority of each
            vertex in the minheap.
        """

        self.size = 0
        self.min_heap = []  # List[Vertex]
        self.vertex_heap_pos = {}  # key - vertex, value -  heap_position
        self.build_heap(dist)

    def left_child(self, i: int) -> int:
        """
        Compute the index of the left child of node i of a 0-based array.

        Parameters
        ----------
        i: int
            Index of a node in the heap

        Returns
        -------
        int:
            Position of left child of node i.
        """
        return (2 * i) + 1

    def parent(self, i: int) -> int:
        """
        Compute the index of the parent of node i of a 0-based array.

        Parameters
        ----------
        i: int
            Index of a node in the heap

        Returns
        -------
        int:
            Position of parent of node i.
        """
        return (i - 1) // 2

    def right_child(self, i: int) -> int:
        """
        Compute the index of the right child of node i of a 0-based array.

        Parameters
        ----------
        i: int
            Index of a node in the heap

        Returns
        -------
        int:
            Position of right child of node i.
        """
        return (2 * i) + 2

    def get_list_vertices_in_heap(self):
        return self.vertex_heap_pos.keys()

    def sift_down(self, i: int) -> None:
        """
        Swap the problematic nodes with a smaller child until the min heap property
        is satisfied.

        Parameters
        ----------
        i: int
            Index of a node in the heap
        """

        min_idx = i

        # compute the index of the left child of i
        left = self.left_child(i)

        # check if i has a left child
        # if the value of the left child is less than the value of the min_idx (current node), change the
        # min_idx to the value of the left child.
        if left < self.size and ((self.min_heap[left].dist < self.min_heap[min_idx].dist) or
                                 ((self.min_heap[left].dist == self.min_heap[min_idx].dist) and
                                  self.min_heap[left].id < self.min_heap[min_idx].id)):
            min_idx = left

        # compute the index of the right child of i
        right = self.right_child(i)

        # check if it has a right child.
        # if the value of the right child is less than the value of the min_idx, change the min_idx
        # to the value of the left child.
        if right < self.size and ((self.min_heap[right].dist < self.min_heap[min_idx].dist) or
                                  (self.min_heap[right].dist == self.min_heap[min_idx].dist and
                                   self.min_heap[right].id < self.min_heap[min_idx].id)):
            min_idx = right

        # if i is not the smallest among its children, swap the node i with the min_idx
        # call swift down on the new swapped element.
        if i != min_idx:
            # update vertex - heap_pos dictionary
            self.vertex_heap_pos[self.min_heap[i].id] = min_idx
            self.vertex_heap_pos[self.min_heap[min_idx].id] = i

            self.min_heap[i], self.min_heap[min_idx] = self.min_heap[min_idx], self.min_heap[i]
            self.sift_down(min_idx)

    def sift_up(self, i: int) -> None:
        """
        Swap the problematic nodes with the parent of node i until the min heap property
        is satisfied.

        Parameters
        ----------
        i: int
            Index of a node in the heap
        """

        parent_idx = self.parent(i)

        # while i is not the root and the value of this node is smaller than the value of its parent, swap
        # the element with its parent.
        while i > 0 and self.min_heap[parent_idx].dist > self.min_heap[i].dist:
            # update vertex - heap_pos dictionary
            self.vertex_heap_pos[self.min_heap[i].id] = parent_idx
            self.vertex_heap_pos[self.min_heap[parent_idx].id] = i

            # swap parent and node i
            self.min_heap[i], self.min_heap[parent_idx] = self.min_heap[parent_idx], self.min_heap[i]

            # assign to the new element
            i = parent_idx
            parent_idx = self.parent(i)

    def insert(self, id: int, dist: Union[int, float]) -> None:
        """
        Insert a new vertex into the heap.

        Parameters
        ----------
        id: int
            Id of the new vertex

        dist: Union[int, float]
            Distance of the new vertex
        """

        # increase heap size
        self.size += 1

        # attach a new node to any leaf
        self.min_heap.append(Vertex(id, dist))
        self.vertex_heap_pos[id] = self.size - 1

        # sift element up to fix any violation (if needed).
        self.sift_up(self.size - 1)

    def build_heap(self, dist: List[Union[int, float]]) -> None:
        """
        Build heap based on the number of vertices on a graph.

        Parameters
        ----------
        dist: List[int]
            List of the distance of each vertex from origin.
        """

        for i in range(len(dist)):
            self.insert(i, dist[i])

    def get_vertex(self) -> Vertex:
        """
        Return the vertex with the lowest priority.

        Returns
        -------
        Vertex:
            Vertex with lowest priority
        """

        # Store the value of the vertex with lowest priority
        result = Vertex(self.min_heap[0].id, self.min_heap[0].dist)

        # replace the root with the rightmost leaf on the last level
        self.vertex_heap_pos[self.min_heap[self.size - 1].id] = 0
        self.min_heap[0] = self.min_heap[self.size - 1]

        # pop the last vertex
        self.min_heap.pop(self.size - 1)

        # decrease size by one
        self.size -= 1

        # sift down the root which was changed by the largest leaf.
        self.sift_down(0)

        # remove the vertex from the heap_pos dictionary
        self.vertex_heap_pos.pop(result.id)

        return result

    def update_dist(self, vertex: int, dist: Union[int, float]) -> None:
        """
        Update the distance from origin to a given vertex.

        Parameters
        ----------
        vertex: int
            Id of the vertex to be updated.
        dist: Union[int, float]
            New distance
        """

        # get position of the given vertex in the min_heap
        pos = self.vertex_heap_pos[vertex]

        # save old distance
        old_dist = self.min_heap[pos].dist

        # assign the new distance to the vertex
        self.min_heap[pos].update_dist(dist)

        # compare the old vs new distance
        if dist > old_dist:
            self.sift_down(pos)
        else:
            self.sift_up(pos)

    def empty(self) -> bool:
        """
        Check min_heap is empty

        Returns
        -------
        bool:
            True if heap is empty, false otherwise.
        """

        return len(self.min_heap) == 0


def minimum_distance(x, y):
    n = len(x)
    # Distance array between origin vertex to each vertex in the graph
    cost = [inf] * n
    # Parent vertex used to arrive to each vertex in the graph
    parent = [None] * n

    # Pick any initial vertex and declare it as root.
    cost[0] = 0

    # create priority queue based on vertex cost, priority is cost.
    q = MinHeap(cost)

    while not q.empty():
        # get vertex with shortest distance value, remote it from the priority queue. Removing it would mean
        # to attach it to the tree.
        u = q.get_vertex()

        # Iterate over all neighbors of u that are present in the priority queue
        for neigh in q.get_list_vertices_in_heap():

            # Calculate the square distance between city u and its neighbor
            calc_dist = distance(x[u.id], x[neigh], y[u.id], y[neigh])

            if cost[neigh] > calc_dist:
                cost[neigh] = calc_dist
                parent[neigh] = u.id

                # change distance (priority)
                q.update_dist(neigh, calc_dist)

    result = 0
    for c in cost:
        result += sqrt(c)

    return result


def distance(x1: int, x2: int, y1: int, y2: int) -> float:
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))