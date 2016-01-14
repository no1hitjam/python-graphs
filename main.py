from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges, directed=False, weighted=False):
        self.vertices = vertices
        self.edges = defaultdict(list)

        def append_edge(v_from, v_to, weight):
            self.edges[v_from].append(Neighbor(v_to, weight))
            if not directed:
                self.edges[v_to].append(Neighbor(v_from, weight))

        if weighted:
            for v_from, v_to, weight in edges:
                append_edge(v_from, v_to, weight)
        else:
            for v_from, v_to in edges:
                append_edge(v_from, v_to, None)

        self.directed = directed


class Edge:
    def __init__(self, v_from, v_to, weight=None):
        self.v_from = v_from
        self.v_to = v_to
        self.weight = weight


class Neighbor:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight


class TreeNode:
    def __init__(self, vertex, children):
        self.vertex = vertex
        self.children = children




