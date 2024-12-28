graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

def breadth_first_print(graph, source):
    queue = [source]
    
    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


#breadth first search practice #1
def breadth_first_search(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

#breadth first search practice #2
def breadth_first_search_two(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        
        for neighbor in graph[current]:
            queue.append(neighbor)

#breadth first search practice #3
def breadth_first_search_three(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

#breadth first search practice #4
def breadth_first_search_four(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

#breadth first search practice #5
def breadth_first_search_five(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

#breadth first search practice #6
def breadth_first_search_6(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        
        for neighbor in graph[current]:
            queue.append(neighbor)







print('Correct:')
breadth_first_print(graph, 'a')
print('Practice:')
breadth_first_search_6(graph, 'a')
    
