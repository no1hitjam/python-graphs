from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, vertices, edges, directed=False, weighted=False):
        # TODO: use _ prefix and use functions for access.
        # assume that users won't access raw properties, just functions
        self._vertices = vertices
        self._edges = edges
        if not directed:
            self._edges.update([Edge(edge.v_to, edge.v_from, edge.weight) for edge in edges])
        self._directed = directed
        self._weighted = weighted

        # testing properties
        self._connected = None  # self._test_connected()
        self._strongly_connected = None  # self._test_strongly_connected()
        self._cyclic = None  # self._test_cyclic()

        # build edge dictionary with vertex_from key
        self._edge_dic = defaultdict(list)
        for edge in self._edges:
            self._edge_dic[edge.v_from].append(edge)

    def update(self, vertices=None, edges=None):
        self._vertices = vertices if vertices is not None else self._vertices
        self._edges = edges if edges is not None else self._edges

        self._connected = self._test_connected()
        self._strongly_connected = self._test_strongly_connected()
        self._cyclic = self._test_cyclic()

    def get_vertices(self): return self._vertices

    def get_edges(self): return self._edges

    def get_edges_from(self, vertex): return self._edge_dic[vertex]

    def is_directed(self): return self._directed
    
    def is_weighted(self): return self._weighted

    def is_connected(self):
        if self._connected is None:
            self._connected = self._test_connected()
        return self._connected

    def is_strongly_connected(self):
        if self._strongly_connected is None:
            self._strongly_connected = self._test_strongly_connected()
        return self._strongly_connected

    def is_cyclic(self):
        if self._cyclic is None:
            self._cyclic = self._test_cyclic()
        return self._cyclic

    def _test_connected(self):
        # check if dfs can hit all vertices
        for vertex in self._vertices:
            if self._vertices.issubset(self.topological_sort(vertex).get_vertices()):
                return True
        return False

    def _test_strongly_connected(self):
        # check if dfs can hit all vertices from every starting position
        for vertex in self._vertices:
            if not self._vertices.issubset(self.topological_sort(vertex).get_vertices()):
                return False
        return True

    def _test_cyclic(self):
        return self.topological_sort() is not None

    def bfs(self, start):
        marked = set()
        queue = deque()
        edges = set()

        queue.append(None, start)
        while len(queue) > 0:
            parent, vertex = queue.popleft()
            if vertex not in marked:
                marked.add(vertex)
                edges.add((parent, vertex))
                for neighbor in self._edges[vertex]:
                    queue.append(vertex, neighbor.vertex)

        return Graph(self.get_vertices(), edges, True)

    def topological_sort(self, start=None, process=None):
        class Status:
            def __init__(self): return
            new = 0
            active = 1
            done = 2

        statuses = {vertex: Status.new for vertex in self._vertices}
        result_edges = set()
        source = 'source'
        vertices = self.get_vertices()
        edges = self.get_edges()

        if start is None:
            start = source
            vertices.add(source)
            # add edges from source to all vertices
            for vertex in self.get_vertices():
                edges.add(Edge(source, vertex))
                statuses[vertex] = Status.new

        def topological_sort_dfs(graph, incoming_edge):
            statuses[incoming_edge.v_to] = Status.active
            for edge in graph.get_edges_from(incoming_edge.v_to):
                if statuses[edge.v_to] == Status.new:
                    if topological_sort_dfs(graph, edge) is False:
                        return False
                elif statuses[edge.v_to] == Status.active:
                    return False  # failure
            statuses[incoming_edge.v_to] = Status.done

            if incoming_edge.v_from is not start:
                result_edges.add(incoming_edge)

            if process is not None:
                process(incoming_edge.v_to)
            return True

        if topological_sort_dfs(Graph(vertices, edges, self._directed, self._weighted), Edge(None, start)) is False:
            return None

        return Graph(self.get_vertices(), result_edges, directed=True)


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
