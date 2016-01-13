from main import Graph
# from shortest_path import dfs
import pygraphviz


def convert_to_pvg(graph):
    py_graph = pygraphviz.AGraph()
    for vertex in graph.vertices:
        py_graph.add_node(vertex)
    #py_graph.add_edge('a', 'd')
    for v_from, v_tos in graph.edges.iteritems():
        for v_to in v_tos:
            py_graph.add_edge(v_from, v_to.vertex)
    return py_graph


def test(number, graph):
    number = str(number)
    pvg = convert_to_pvg(graph)
    pvg.layout()
    pvg.draw('test results/test' + number + '.png')
    print('wrote test' + number + '.png')


test('001', Graph({'a', 'b', 'c', 'd'}, {
                    ('a', 'b'),
                    ('c', 'd'),
                    ('d', 'b'),
                    ('c', 'a')}))

