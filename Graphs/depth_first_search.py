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


def recursive_depth_first_search_practice_one(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_one(graph, neighbor)


def recursive_depth_first_search_practice_two(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_two(graph, neighbor)


def recursive_depth_first_search_practice_three(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_three(graph, neighbor)


def iterative_depth_first_search_practice_two(graph, source):
    stack = [source]
    
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

def recursive_depth_first_search_practice_four(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_four(graph, neighbor)



def iterative_depth_first_search_practice_three(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


def  recursive_depth_first_search_practice_five(graph, source):
    print(source)

    for neighbor in graph[source]:
        recursive_depth_first_search_practice_five(neighbor, source)


print('\t Recursive')
recursive_depth_first_search_practice_four(graph, 'a')
#recursive_depth_first_print(graph, 'a')
print('\t Iterative')
iterative_depth_first_search_practice_three(graph, 'a')
#iterative_depth_first_print(graph, 'a')
#recursive_depth_first_search_practice_one(graph, 'a')
#print(graph)
#recursive_depth_first_search_practice_three(graph, 'a')
#iterative_depth_first_search_practice_two(graph, 'a')

