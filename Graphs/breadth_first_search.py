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




breadth_first_print(graph, 'a')
print('\t Practice')
breadth_first_search(graph, 'a')
    