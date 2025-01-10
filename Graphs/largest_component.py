graph = {
    0: [5, 1, 8],
    1: [0],
    2: [4, 3],
    3: [4, 2],
    4: [2, 3],
    5: [0, 8],
    8: [5, 0],
}

#larget component 1
def largest_components(graph):
    longest = 0
    visited = set()

    for node in graph:
        size = countSize(graph, node, visited)
        if size > longest:
            longest = size
    
    return longest

def countSize(graph, node, visited):
    if node in visited:
        return 0
    
    visited.add(node)

    size = 1

    for neighbor in graph[node]:
       size += countSize(graph, neighbor, visited)

    return size
    
#largest component practice 2
def largest_component_2(graph):
    visited = set()
    largest = 0

    for node in graph:
        size = count_island(graph, node, visited)
        if size > largest:
            largest = size
    
    return largest

def count_island(graph, node, visited):
    if node in visited:
        return 0
        
    visited.add(node)

    size = 1

    for neighbor in graph[node]:
        size += count_island(graph, neighbor, visited)
    
    return size


    
print('Correct:', largest_components(graph))
print('Practice: ', largest_component_2(graph))
