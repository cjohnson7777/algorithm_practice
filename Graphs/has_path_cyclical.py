graph = {
        'i': ['j', 'k'], 
        'j': ['i'], 
        'k': ['i', 'm', 'l'], 
        'm': ['k'],
        'l': ['k'], 
        'o': ['n'], 
        'n': ['o']
}

#has path cyclical
def has_path_c(graph, src, dst, visited):    
    if src == dst:
        return True
    
    if src in visited:
        return False
     
    visited.add(src)

    for neighbor in graph[src]:
        if has_path_c(graph, neighbor, dst, visited) == True:
            return True
        
    return False

#has path cyclical practice #2
def has_path_c_two(graph, src, dst, visited):   
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)

    for neighbor in graph[src]:
        if has_path_c_two(graph, neighbor, dst, visited) == True:
            return True
    
    return False

#has path cyclical practice #3
def has_path_c_3(graph, src, dst, visited):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)

    for neighbor in graph[src]:
        if has_path_c_3(graph, neighbor, dst, visited) == True:
            return True
    
    return False

#has path cyclical practice #4
def has_path_c_4(graph, src, dst, visited):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)

    for neighbor in graph[src]:
        if (has_path_c(graph, neighbor, dst, visited)) == True:
            return True
    
    return False


#has path cyclical practice #1
print('Correct: ', has_path_c(graph, 'i', 'k', set()))
print('Practice: ', has_path_c_4(graph, 'i', 'k', set()))


