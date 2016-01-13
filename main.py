"""
class Graph:
    def __init__(self, vertices, edges, directed=False):
        self.vertices = vertices
        self.edges = {}
        for edge in edges:
            if edge.v_from in edges:
                edges[edge.v_from].add(Neighbor(edge.v_to, edge.weight))
            else:
                edges[edge.v_from] = {Neighbor(edge.v_to, edge.weight)}
            if not directed:
                if edge.v_to in edges:
                    edges[edge.v_to].add(Neighbor(edge.v_from, edge.weight))
                else:
                    edges[edge.v_to] = {Neighbor(edge.v_from, edge.weight)}
        self.directed = directed
"""

from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges, directed=False):
        self.vertices = vertices
        self.edges = defaultdict(list)
        for edge in edges:
            edges[edge.v_from].append(Neighbor(edge.v_to, edge.weight))
            if not directed:
                    edges[edge.v_to].append(Neighbor(edge.v_from, edge.weight))
        self.directed = directed


class Edge:
    def __init__(self, v_from, v_to, weight=None):
        self.v_from = v_from
        self.v_to = v_to
        self.weight = weight


class Neighbor:
    def __init__(self, to, weight=None):
        self.to = to
        self.weight = weight


class TreeNode:
    def __init__(self, vertex, children):
        self.vertex = vertex
        self.children = children




