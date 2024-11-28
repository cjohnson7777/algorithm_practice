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

#depth first has path practice recursive #1
def has_path_depth_two(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path_depth_two(graph, neighbor, dst) == True:
            return True
    return False
        

#depth first has path practice iterative #1
def has_path_depth_three(graph, src, dst):
    stack = [src]

    while stack:
        current = stack.pop(0)
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False

#has path depth recursive practice #2
def has_path_depth_four(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path_depth_four(graph, neighbor, dst) == True:
            return True
    
    return False

def has_path_depth_five(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path_depth_five(graph, neighbor, dst) == True:
            return True
    
    return False





#print(has_path_depth(graph, 'f', 'k'))
#print(has_path_breadth(graph, 'f', 'k'))
#print(has_path_breadth_two(graph, 'f', 'k'))
#print(has_path_depth_two(graph, 'f', 'k'))
print(has_path_depth_four(graph, 'f', 'j'))
