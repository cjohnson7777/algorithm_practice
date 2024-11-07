graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': [],
}

#depth first search
def has_path_depth(graph, src, dst):
    if src == dst: 
        return True
    
    for neighbor in graph[src]:
        if has_path_depth(graph, neighbor, dst) == True:
            return True
        
    return False

#breadth first search
def has_path_breadth(graph, src, dst):
    queue = [src]

    while queue:
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False

#breadth first has_path practice #1
def has_path_breadth_two(graph, src, dst):
    queue = [src]

    while queue:
        current = queue.pop(0)
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False



#print(has_path_depth(graph, 'f', 'k'))
#print(has_path_breadth(graph, 'f', 'k'))
print(has_path_breadth_two(graph, 'f', 'k'))
