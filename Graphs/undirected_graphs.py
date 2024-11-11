#Edge list
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

#convert edge list to adjacency list
def build_graph(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph        

#traversal through path gaurding against infinit loops 
def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    
    if src in visited:
        return False
     
    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True
        
    return False


#has path in undirected graph function
def undirected_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    return has_path(graph, nodeA, nodeB, set())

print(undirected_path(edges, 'f', 'k'))
