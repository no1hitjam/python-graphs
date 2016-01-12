def basic_dfs(vertex, graph):
    if vertex not in graph.marked:
        graph.mark(vertex)
        for neighbor in graph.edges[vertex]:
            basic_dfs(neighbor.vertex, graph)


def advanced_dfs(vertex, graph):
    graph.mark(vertex)
    # pre_visit(v)
    for neighbor in graph.edges[vertex]:
        if vertex not in graph.marked:
            graph.parent(neighbor.vertex, vertex)
            advanced_dfs(neighbor.vertex, graph)
    # post_visit(v)


class Graph:
    def __init__(self, vertices, edges, directed=False):
        self.vertices = vertices
        self.marked = set()
        self.parents = {}
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

    def mark(self, vertex):
        self.marked.add(vertex)

    def parent(self, vertex, parent):
        self.parents[parent] = vertex

    def get_forest(self):
        def add_children(node):
            for child in self.parents[node.vertex]:
                child_node = TreeNode(child, set())
                node.children.add(child_node)
                add_children(child_node)
        for s in self.vertices.difference(self.parents.keys()):
            start_node = TreeNode(s, set())
            add_children(start_node)


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
