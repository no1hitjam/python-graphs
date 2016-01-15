import random
from collections import defaultdict
from collections import deque

from main import Graph


def bfs(graph, start):
    marked = set()
    queue = deque()
    edges = set()

    queue.append(None, start)
    while len(queue) > 0:
        parent, vertex = queue.popleft()
        if vertex not in marked:
            marked.add(vertex)
            edges.add((parent, vertex))
            for neighbor in graph.edges[vertex]:
                queue.append(vertex, neighbor.vertex)

    return Graph(graph.get_vertices(), edges, True)


def topological_sort(graph, start=None, process=None):
    class Status:
        new = 0
        active = 1
        done = 2

    statuses = {}
    order = []
    tree_edges = set()
    source = 'source'
    vertices = graph.get_vertices()
    edges = graph.get_edges()

    if start is None:
        start = source
        vertices.add(source)
        # add edges from source to all vertices
        for vertex in graph.get_vertices():
            edges.add((source, vertex))
            statuses[vertex] = Status.new

    def topological_sort_dfs(vertex, graph):
        statuses[vertex] = Status.active
        for edge in graph.get_edges()[vertex]:
            if statuses[edge.v_to] == Status.new:
                topological_sort_dfs(edge.v_to, graph)
            elif statuses[edge.v_to] == Status.active:
                return None  # failure
        statuses[vertex] = Status.done
        order.append(vertex)
        if process is not None:
            process(vertex)

    topological_sort_dfs(start, Graph(vertices, edges))
    order.reverse()
    return order






