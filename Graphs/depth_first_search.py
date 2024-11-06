graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

def iterative_depth_first_print(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

def recursive_depth_first_print(graph, source):
    print(source)

    for neighbor in graph[source]:
        recursive_depth_first_print(graph, neighbor)



def iterative_depth_first_search(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


def recursive_depth_first_search(graph, source):
    print(source)
 
    for neighbor in graph[source]:
        recursive_depth_first_search(graph, neighbor)


print('\t Recursive')
recursive_depth_first_print(graph, 'a')
print('\t Iterative')
iterative_depth_first_print(graph, 'a')