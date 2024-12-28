#Edge list
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

#build graph practice #1
def build_graph_one(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph 

#build graph practice #2
def build_graph_two(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

#build graph practice #3
def build_graph_three(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

#build graph practice #4
def build_graph_four(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)

    return graph


#build graph practice #5
def build_graph_five(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

print('Correct: ', build_graph_one(edges))
print('Correct: ', build_graph_five(edges))

