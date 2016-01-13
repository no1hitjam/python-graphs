from main import Graph
from main import TreeNode
from search import dfs

import pygraphviz


def convert_graph_to_pvg(graph):
    pvg = pygraphviz.AGraph()
    for vertex in graph.vertices:
        pvg.add_node(vertex)
    for v_from, v_tos in graph.edges.iteritems():
        for v_to in v_tos:
            pvg.add_edge(v_from, v_to.vertex)
    return pvg


def convert_tree_to_pvg(root):
    pvg = pygraphviz.AGraph()

    def convert_node(node):
        pvg.add_node(node.vertex)
        for child_node in node.children:
            convert_node(child_node)
            pvg.add_edge(node.vertex, child_node.vertex)

    convert_node(root)
    return pvg


def test(number, graph):
    number = str(number)
    if isinstance(graph, Graph):
        pvg = convert_graph_to_pvg(graph)
    elif isinstance(graph, TreeNode):
        pvg = convert_tree_to_pvg(graph)
    else:
        pvg = pygraphviz.AGraph()
    pvg.layout()
    pvg.draw('test results/test' + number + '.png')
    print('wrote test' + number + '.png')


test('001', Graph({'a', 'b', 'c', 'd'}, {
                    ('a', 'b'),
                    ('c', 'd'),
                    ('d', 'b'),
                    ('c', 'a')}))

test('002', dfs('a', Graph({'a', 'b', 'c', 'd'}, {
                            ('a', 'b'),
                            ('c', 'd'),
                            ('d', 'b'),
                            ('c', 'a')})))
