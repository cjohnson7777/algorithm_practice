import queue


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v'],
    ['r', 'q'],
]

graph1 = {
          'w': ['x', 'v'], 
          'x': ['w', 'y'], 
          'y': ['x', 'z'], 
          'z': ['y', 'v'], 
          'v': ['z', 'w']
}

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

#shortest path 1
def shortest_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    visited = set(nodeA)

    distance = 0
    queue = [[nodeA, distance]]

    while queue:
        node, distance = queue.pop(0)

        if node == nodeB:
            return node, distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])
    
    return -1

#shortest path 2
def shortest_path_2(graph, nodeA, nodeB):
    distance = 0
    queue = [[nodeA, distance]]
    visited = set(nodeA)

    while queue:
        node, distance = queue.pop(0)

        if node == nodeB:
            return node, distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])

#shortest path 3
def shortest_path_3(graph, nodeA, nodeB):
    distance = 0
    visited = set(nodeA)
    queue = [[nodeA, distance]]

    while queue:
        node, distance = queue.pop(0)

        if node == nodeB:
            return node, distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])


print('Correct: ', shortest_path(edges, 'w', 'z'))
print('Practice: ', shortest_path_3(graph1, 'w', 'z'))
     



