"""
Week 1
Tuesday
"""
import search


"""
G:graph = (V:vertices, E:edges)
Vertices are neighbors if they have an edge between
Walk between vertices if edges connected through
Path: walk with no repeated vertex
"""


def test_path(vertex1, vertex2, graph):
    marked = search.dfs_marked(vertex1, graph)
    return vertex2 in marked


# G is connected if there is path between any two vertices
def test_connected(graph):
    return len(graph.vertices.difference(search.dfs_marked(graph.vertices.pop(), graph))) == 0



"""
G' is a subgraph of G if V' and E' are subsets of V and E
Connected components of G are maximal connected subgraph of G
Cycle: A path with identical endpoints
G is acyclic if it doesn't contain a cycle (forest)
G is a tree if it is connected and acyclic
Vertex degree is # of neighbors
Simple graph: no loops or parallel edges
Adjacency matrix (1,0)
Adjacency linked list
DFS: search for paths with stack
BFS: search for paths with queue

Thursday
G is a directed, acyclic graph (DAG) if G does not contain any directed cycle.
To test for DAG
Do a depth first search to create a tree from the directed graph
Look at edges not in graph
    Forward edge (ancestor to descendant)
    Backward edge (descendant to ancestor)
    There is a cycle
    Cross edge (cousins)
You can mark edges with 'time' accessed going forward and back and compare with that to see if there is a backward edge
Strongly connected (directed graph): Go from any vertex to any vertex
"""