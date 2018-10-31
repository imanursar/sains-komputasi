parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if (root1 != root2):
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if (rank[root1] == rank[root2]):
            rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
        minimum_spanning_tree = set()

    edges = list(graph['edges'])
    edges.sort()

	    #print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge

        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)

graph_1 = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
'edges': set([
(4, 'A', 'B'),
(8, 'B', 'C'),
(7, 'C', 'D'),
(4, 'C', 'F'),
(2, 'C', 'I'),
(11, 'B', 'H'),
(9, 'D', 'E'),
(14, 'D', 'F'),
(10, 'E', 'F'),
(2, 'F', 'G'),
(6, 'G', 'I'),
(1, 'G', 'H'),
(7, 'H', 'I'),
(8, 'A', 'H')
])
}

graph_2 = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
'edges': set([
(4, 'A', 'B'),
(8, 'B', 'C'),
(5, 'B', 'I'),
(7, 'C', 'D'),
(4, 'C', 'F'),
(2, 'C', 'I'),
(11, 'B', 'H'),
(9, 'D', 'E'),
(14, 'D', 'F'),
(10, 'E', 'F'),
(2, 'F', 'G'),
(6, 'G', 'I'),
(1, 'G', 'H'),
(7, 'H', 'I'),
(8, 'A', 'H')
])
}

graph_3 = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
'edges': set([
(4, 'A', 'B'),
(8, 'B', 'C'),
(5, 'B', 'I'),
(7, 'C', 'D'),
(4, 'C', 'F'),
(2, 'C', 'I'),
(11, 'B', 'H'),
(9, 'D', 'E'),
(6, 'D', 'G'),
(14, 'D', 'F'),
(10, 'E', 'F'),
(2, 'F', 'G'),
(6, 'G', 'I'),
(1, 'G', 'H'),
(7, 'H', 'I'),
(8, 'A', 'H')
])
}

graph_4 = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
'edges': set([
(4, 'A', 'B'),
(8, 'B', 'C'),
(5, 'B', 'I'),
(7, 'C', 'D'),
(4, 'C', 'F'),
(2, 'C', 'I'),
(11, 'B', 'H'),
(9, 'D', 'E'),
(14, 'D', 'F'),
(4, 'D', 'I'),
(4, 'F', 'I'),
(10, 'E', 'F'),
(2, 'F', 'G'),
(6, 'G', 'I'),
(1, 'G', 'H'),
(7, 'H', 'I'),
(8, 'A', 'H')
])
}

print (kruskal(graph_1))
print (kruskal(graph_2))
print (kruskal(graph_3))
print (kruskal(graph_4))
