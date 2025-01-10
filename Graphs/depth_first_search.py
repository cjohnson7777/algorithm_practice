graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

#iterative depth first search #1
def iterative_depth_first_print(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

#recursive depth first search #1
def recursive_depth_first_print(graph, source):
    print(source)

    for neighbor in graph[source]:
        recursive_depth_first_print(graph, neighbor)

#iterative depth first search #2
def iterative_depth_first_search(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

#recursive depth first search #2
def recursive_depth_first_search(graph, source):
    print(source)
 
    for neighbor in graph[source]:
        recursive_depth_first_search(graph, neighbor)

#recursive depth first search #3
def recursive_depth_first_search_practice_three(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_three(graph, neighbor)


#recursive depth first search #4
def recursive_depth_first_search_practice_four(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_four(graph, neighbor)


#recursive depth first search #5
def recursive_depth_first_search_practice_five(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_five(graph, neighbor)

#iterative depth first search #2
def iterative_depth_first_search_practice_two(graph, source):
    stack = [source]
    
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

#recursive depth first search #6
def recursive_depth_first_search_practice_six(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursive_depth_first_search_practice_six(graph, neighbor)

#iterative depth first search #3
def iterative_depth_first_search_practice_three(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

#recursive depth first search #7
def  recursive_depth_first_search_practice_seven(graph, source):
    print(source)

    for neighbor in graph[source]:
        recursive_depth_first_search_practice_seven(neighbor, source)

#recursive depth first search #7
def recursive_depth_first_search_practice_seven(graph, source):
    print(source)

    for neighbor in graph[source]:
        recursive_depth_first_search_practice_seven(graph, neighbor)

#recursive depth first search #8
def recursive_depth_first_search_practice_8(graph, source):
    print(source)

    for neighbor in graph[source]:
        recursive_depth_first_search_practice_8(graph, neighbor)

#iterative depth first search 4
def iterative_depth_first_search_practice_4(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)






print('\t Correct Recursive')
recursive_depth_first_print(graph, 'a')

# print('\t Iterative Correct')
# iterative_depth_first_print(graph, 'a')

# print('\t Iterative Practice')
# iterative_depth_first_search_practice_4(graph, 'a')

print('\t Practice Recursive')
recursive_depth_first_search_practice_8(graph, 'a')



