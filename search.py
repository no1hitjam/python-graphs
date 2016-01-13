

from collections import defaultdict
from collections import deque

from main import TreeNode


def get_forest(parents, graph):
    trees = set()

    def add_children(node):
        for child in parents[node]:
            child_node = TreeNode(child, set())
            node.children.add(child_node)
            add_children(child_node)

    for start in graph.vertices.difference(parents.keys()):
        start_node = TreeNode(start, set())
        add_children(start_node)
        trees.add(start_node)

    return trees


def get_tree(parents, graph):
    forest = get_forest(parents, graph)
    if len(forest) == 1:
        return forest.pop()
    else:
        raise Exception('Did not find single tree')


def simple_dfs(start, graph):
    marked = set()

    def basic_dfs_rec(vertex):
        if vertex not in marked:
            marked.add(vertex)
            for neighbor in graph.edges[vertex]:
                basic_dfs_rec(neighbor.vertex)

    basic_dfs_rec(start)
    return marked


def dfs(start, graph):
    marked = set()
    parents = defaultdict(list)

    def advanced_dfs_rec(vertex):
        marked.add(vertex)
        # pre_visit(v)
        for neighbor in graph.edges[vertex]:
            if vertex not in marked:
                parents[vertex].append(neighbor.vertex)
                advanced_dfs_rec(neighbor.vertex)
        # post_visit(v)

    advanced_dfs_rec(start)
    return get_tree(parents, graph)


def bfs(start, graph):
    marked = set()
    queue = deque()
    parents = defaultdict(list)

    queue.append(None, start)  # put (NULL, s) in bag
    while len(queue) > 0:
        parent, vertex = queue.popleft()
        if vertex not in marked:
            marked.add(vertex)
            parents[parent].append(vertex)
            for neighbor in graph.edges[vertex]:
                queue.append(vertex, neighbor.vertex)

    return get_tree(parents, graph)
