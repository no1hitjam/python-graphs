"""
SHORTEST PATH

input:  directed, weighted graph
output: shortest path from s to all vertices
        for each vertex return distance and predecessor vertex. This creates a tree

more:   suppose G is a DAG
O(E+V)      do a topological sort
O(V)        for i <- 1 to V
                dist[i] <-
O(E)                min (from j->i in E) [dist[j] + w(j->i)]
        (in English, distance to a vertex is the minimum of distance to all vertices (that occur earlier in the sort)
            + distance from that vertex to the final vertex)

for i <- 1 to V
    for all j->i in E
        if dist[i] > dist[j] + weight(j->i)
            dist[i] <- dist[j] + weight(j->i)


j->i in E is tense if dist[i] > dist[j] + weight(j -> i)

relax(j -> i)
    predecessor(i) -< j
    dist[i] <- dist[j] + w(j->i)

shortest path: relax all tense edges

dist(s) <- 0
predecessor(s) <- null
for all v in V
    dist(v) <- infinity
    predecessor(v) <- null
while exists a tense j->i in E
    relax(j->i)


Djkstra(G,s)
    Init
    while(Exists an unmarked certex
        v <- the unmarked vertex with min dist value
        for all v -> u
            if v->u is tense
                relax(v->u)
        mark(v)

exercise: prove Dijkstra correctly computes shortest path if there exists no negative edge


Shimbel(G,s)
    Init
    for i <- 1 to V
        for all u->v in E
            if u->v is tense
                relax(u->v)

O(V*E) and works for negative edges


"""

