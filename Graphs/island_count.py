#time complexity: O(rc) rows/columns
#space complexity: O(rc)

matrix = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w'],
]

#island count 1
def island_count(matrix):
    count = 0
    visited = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if explore_island(matrix, i, j, visited) == True:
                count += 1
    return count

def explore_island(matrix, i, j, visited):
    rowInBounds = i >= 0 and i < len(matrix)
    colInBounds = j >= 0 and j < len(matrix[0])
    
    if not (rowInBounds and colInBounds):
        return False
    
    if matrix[i][j] == 'w':
        return False

    if (i, j) in visited:
        return False
    
    visited.add((i, j))

    explore_island(matrix, i - 1, j, visited)
    explore_island(matrix, i + 1, j, visited)
    explore_island(matrix, i, j - 1, visited)
    explore_island(matrix, i, j + 1, visited)

    return True

#island count 2
def island_count_2(matrix):
    visited = set()
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if explore_island_2(matrix, i, j, visited) == True:
                count += 1
    
    return count

def explore_island_2(matrix, i, j, visited):
    rowInBound = i >= 0 and i < len(matrix)
    colInBound = j >= 0 and j < len(matrix[0])

    if not (rowInBound and colInBound):
        return False
    
    if matrix[i][j] == 'w':
        return False
    
    if (i, j) in visited:
        return False
    
    visited.add((i, j))

    explore_island_2(matrix, i + 1, j, visited)
    explore_island_2(matrix, i - 1, j, visited)
    explore_island_2(matrix, i, j + 1, visited)
    explore_island_2(matrix, i, j - 1, visited)

    return True



print('Correct:', island_count(matrix))
print('Practice:', island_count_2(matrix))



    


    



