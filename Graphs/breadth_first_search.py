
graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}
#bread first search
def breadth_first_search(graph, source):
    queue = [source]
    
    while queue:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


#breadth first search practice #7
def breadth_first_search7(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        
        for neighbor in graph[current]:
            queue.append(neighbor)
        


print('Correct:')
breadth_first_search(graph, 'a')
print('Practice:')
breadth_first_search7(graph, 'a')
    
