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

O(E+V*log(v))

exercise: prove Dijkstra correctly computes shortest path if there exists no negative edge


Shimbel(G,s)
    Init
    for i <- 1 to V
        for all u->v in E
            if u->v is tense
                relax(u->v)

O(V*E) and works for negative edges


Day 2:

All shortest paths
    input: graph with no negative cycles
    output: distance between any two pairs. Will be a matrix
    you can use Djkstra or Shimbel for all vertices

Johnson's algorithm:
    let c be a set of any number selected for each vertex
    let w' of an edge u->v be its weight - c(u) + c(v)
    let P be any shortest path with respect to w
    then P is a shortest path with respect to w'

    w(u->v) + c(u) - c(v) >= 0
        => c(v) <= c(u) + w(u->v)

    Use Shimbel to find shortest path for one vertex, use that to find Johnson's vertex values (each vertex value is
    just the shortest path for each vertex), update the edges based on the c-values, then use Djikstra for the rest of
    the vertices.


Dynamic Programming:
                    VALUE               IF...
    dist[u,v,k] =    {0               u = v
                      inf             k=0, u != v

                      min(x->v) in E: [dist[u,x, k-1] + w(x->v)]]

    dist[u,v,k] =       {0              u = v
                         inf            k = 0, u !=v

                         min x in V: [dist[u,x,k/2] + dist[x,v,k/2]]
        note: k should be nearest power of 2
    O(V*V*V*logV)

Floyd Marshall:
    dist[u,v,r]
    Assume V={1,2,...v}
    The length of the shortest uv-path whose intermediate vertices is a subset of {1,2,...,r}

    dist[u,v,r] =   {w(u->v),       r=0
                     min [dist(u,v,r-1), dist(u,r,r-1)+dist(r,v,r-1)]

            (for r<-1 to V
                for u in V
                    for v in V)

    O(V*V*V)

"""

