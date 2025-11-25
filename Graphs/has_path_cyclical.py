graph = {
        'i': ['j', 'k'], 
        'j': ['i'], 
        'k': ['i', 'm', 'l'], 
        'm': ['k'],
        'l': ['k'], 
        'o': ['n'], 
        'n': ['o']
}

#has path cyclical recursive
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

#has path cyclical recursive practice
def has_path_5(graph, src, dst, vistited):
    if src == dst:
        return True
    
    if src in vistited:
        return False
    
    vistited.add(src)

    for neighbor in graph[src]:
        if has_path_5(graph, neighbor, dst, vistited) == True:
            return True
    
    return False






print('Correct: ', has_path_c(graph, 'i', 'k', set()))
print('Practice: ', has_path_5(graph, 'i', 'k', set()))


