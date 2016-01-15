import random
from collections import defaultdict

import search


class Graph:
    def __init__(self, vertices, edges, directed=False, weighted=False):
        # TODO: use _ prefix and use functions for access.
        # assume that users won't access raw properties, just functions
        self._vertices = vertices
        self._edges = defaultdict(list)
        self._directed = directed
        self._weighted = weighted
        self._connected = self._test_connected()
        self._strongly_connected = self._test_strongly_connected()
        self._cyclic = self._test_cyclic()

        for v_from, v_to, weight in edges:
            self._edges[v_from].append(Neighbor(v_to, weight if weighted else None))
            if not directed:
                self._edges[v_to].append(Neighbor(v_from, weight if weighted else None))

    def update(self, vertices=None, edges=None):
        self._vertices = vertices if vertices is not None else self._vertices
        self._edges = edges if edges is not None else self._edges

        self._connected = self._test_connected()
        self._strongly_connected = self._test_strongly_connected()
        self._cyclic = self._test_cyclic()

    def get_vertices(self): return self._vertices

    def get_edges(self): return self._edges

    def is_directed(self): return self._directed
    
    def is_weighted(self): return self._weighted

    def is_connected(self): return self._connected

    def is_strongly_connected(self): return self._strongly_connected

    def is_cyclic(self): return self._cyclic

    def _test_connected(self):
        # check if dfs can hit all vertices
        for vertex in self._vertices:
            if self._vertices.issubset(search.topological_sort(self, vertex).get_vertices()):
                return True
        return False

    def _test_strongly_connected(self):
        # check if dfs can hit all vertices from every starting position
        for vertex in self._vertices:
            if not self._vertices.issubset(search.topological_sort(self, vertex).get_vertices()):
                return False
        return True

    def _test_cyclic(self):
        return search.topological_sort(self) is not None


class Edge:
    def __init__(self, v_from, v_to, weight=None):
        self.v_from = v_from
        self.v_to = v_to
        self.weight = weight

    def __str__(self):
        if self.weight is None:
            return str(self.v_from) + ' --> ' + str(self.v_to)
        else:
            return str(self.v_from) + ' --(' + str(self.weight) + ')->' + str(self.v_to)


class Neighbor:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return str(self.vertex) + (str(self.weight) if self.weight is not None else "")


class TreeNode:
    def __init__(self, vertex, children=None):
        self.vertex = vertex
        self.children = children if children is not None else set()

    def __str__(self):
        rep = str(self.vertex) + '--('
        for child in self.children:
            rep += str(child.vertex)
        rep += ')'
        return rep




