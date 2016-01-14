from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges, directed=False, weighted=False):
        # TODO: use _ prefix and use functions for access.
        # assume that users won't access raw properties, just functions
        self.vertices = vertices
        self.edges = defaultdict(list)
        self.directed = directed
        self._weighted = weighted

        for v_from, v_to, weight in edges:
            self.edges[v_from].append(Neighbor(v_to, weight if weighted else None))
            if not directed:
                self.edges[v_to].append(Neighbor(v_from, weight if weighted else None))

        self._update()

    def update(self, vertices=None, edges=None):
        self.vertices = vertices if vertices is not None else self.vertices
        self.edges = edges if edges is not None else self.edges

        # self.cyclic = self._test_cyclic()
        # self.connected = self._test_connected()

    def is_directed(self): return self.directed
    
    def is_weighted(self): return self._weighted

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




