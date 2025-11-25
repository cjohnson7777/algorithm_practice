graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

#iterative depth first search
def depth_first_search_i(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

#recursive depth first search
def depth_first_search_r(graph, source):
    print(source)

    for neighbor in graph[source]:
        depth_first_search_r(graph, neighbor)

#iterative depth first practice 
def depth_first_search_i_4(graph, source):
    stack = [source]
    
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

#recursive depth first practice 
def depth_first_search_r_10(graph, source):
    print(source)

    for neighbor in graph[source]:
        depth_first_search_r_10(graph, neighbor)


print('\t Correct Recursive')
depth_first_search_r(graph, 'a')

print('\t Practice Recursive')
depth_first_search_r_10(graph, 'a')

# print('\t Iterative Correct')
# depth_first_search_i(graph, 'a')

# print('\t Iterative Practice')
# depth_first_search_i_4(graph, 'a')





