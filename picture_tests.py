from main import Graph
from main import Edge

import pygraphviz


def convert_graph_to_pvg(graph):
    pvg = pygraphviz.AGraph()
    for vertex in graph.get_vertices():
        pvg.add_node(vertex)
    for edge in graph.get_edges():
        pvg.add_edge(edge.v_from, edge.v_to)
    return pvg


def test(number, graph):
    pvg = convert_graph_to_pvg(graph)
    pvg.layout()
    pvg.draw('test results/test' + number + '.png')
    print('wrote test' + number + '.png')


test('001', Graph({'a', 'b', 'c', 'd'}, {
                    Edge('a', 'b'),
                    Edge('c', 'd'),
                    Edge('d', 'b'),
                    Edge('c', 'a')}))

test('002', Graph.topological_sort(Graph({'a', 'b', 'c', 'd'}, {
                            Edge('a', 'b'),
                            Edge('c', 'd'),
                            Edge('d', 'b')}, directed=True), 'a'))

test('003', Graph({'a', 'b', 'c', 'd', 'e'}, {
                    Edge('a', 'b'),
                    Edge('c', 'd'),
                    Edge('d', 'b'),
                    Edge('c', 'a')}, True))
