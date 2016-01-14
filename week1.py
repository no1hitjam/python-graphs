"""

Week 1
Tuesday
Îù G:graph = (V:vertices, E:edges)
Îù Vertices are neighbors if they have an edge between
Îù Walk between vertices if edges connected through
Îù Path: walk with no repeated vertex
Îù G is connected if there is path between any two vertices
Îù G' is a subgraph of G if V' and E' are subsets of V and E 
Îù Connected components of G are maximal connected subgraph of G 
Îù Cycle: A path with identical endpoints
Îù G is acyclic if it doesn't contain a cycle (forest)
Îù G is a tree if it is connected and acyclic
Îù Vertex degree is # of neighbors
Îù Simple graph: no loops or parallel edges
Îù Adjacency matrix (1,0)
Îù Adjacency linked list
Îù DFS: search for paths with stack
Îù BFS: search for paths with queue
Thursday
Îù G is a directed, acyclic graph (DAG) if G does not contain any directed cycle.
Îù To test for DAG
Î÷ Do a depth first search to create a tree from the directed graph
Î÷ Look at edges not in graph
ÎåÎá Forward edge (ancestor to descendant)
ÎåÎá Backward edge (descendant to ancestor)
ÎõÎé There is a cycle
ÎåÎá Cross edge (cousins)
Î÷ You can mark edges with 'time' accessed going forward and back and compare with that to see if there is a backward edge
Îù Strongly connected (directed graph): Go from any vertex to any vertex
Î÷ 



"""
