from itertools import count


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


#connected components count 1
def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        print(visited)
        if explore(graph, node, visited) == True:
            count += 1
    
    return count

def explore(graph, current, visited):
    if current in visited:
        return False 
    
    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    
    return True


print('Correct: ',connected_components_count(graph))

#connected components count 2
def connected_components_practice_2(graph):
    count = 0
    visited = set()

    for node in graph:
        if explore_practice_2(graph, node, visited) == True:
            count += 1
    
    return count

def explore_practice_2(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore_practice_2(graph, neighbor, visited)
    
    return True

#connected components count 3
def connected_components_count_practice3(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore_practice_3(graph, node, visited) == True:
            count += 1

    return count


def explore_practice_3(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore_practice_3(graph, neighbor, visited)
    
    return True
    
#connected components count 4
def connected_components_count_4(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore_practice_4(graph, node, visited) == True:
            count += 1
    
    return count


def explore_practice_4(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)

    for neighbor in graph[current]:
        explore_practice_4(graph, neighbor, visited)
    
    return True

#connected components count 5
def connected_components_count_5(graph):
    visted = set()
    count = 0

    for node in graph:
       if explore_practice_5(graph, node, visted) == True:
           count += 1
    
    return count
       

def explore_practice_5(graph, current, visited):
    if current in visited:
        return False
    
    visited.add(current)
    
    for neighbor in graph[current]:
        explore_practice_5(graph, neighbor, visited)
    
    return True


print('Practice: ', connected_components_count_5(graph))