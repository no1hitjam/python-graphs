from main import Graph
# from shortest_path import dfs
import pygraphviz

test_graph1 = Graph({'a', 'b', 'c', 'd'}, {('a', 'b'), ('c', 'd'), ('d', 'b')})


def display(graph):
    py_graph = pygraphviz.AGraph()
    for vertex in graph.vertices:
        py_graph.add_node(vertex)
    for edge in graph.edges:
        py_graph.add_edge(edge.v_from, edge.v_to)
    return py_graph

display(test_graph1)
