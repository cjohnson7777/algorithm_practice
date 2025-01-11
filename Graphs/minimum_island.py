#Time: O(rc) row/col
#Space: O(rc) 


import math


grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w'],
]

#minumum island 1
def minimum_island(grid):
    visited = set()
    smallest = math.inf

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreIsland(grid, r, c, visited)
            if size > 0 and size < smallest:
                smallest = size
    
    return smallest

def exploreIsland(grid, r, c, visited):
    rowInBound = r >= 0 and r < len(grid)
    colInBound = c >= 0 and c < len(grid[0])

    if not rowInBound or not colInBound: 
        return 0
    
    if grid[r][c] == 'w':
        return 0
    
    if (r, c) in visited:
        return 0
    
    visited.add((r, c))

    size = 1

    size += exploreIsland(grid, r - 1, c, visited)
    size += exploreIsland(grid, r + 1, c, visited)
    size += exploreIsland(grid, r, c - 1, visited)
    size += exploreIsland(grid, r, c + 1, visited) 

    return size





#minimum island 2
def minimum_island2(matrix):
    visited = set()
    minimum = math.inf

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            size = exploreIsland2(matrix, i, j, visited)
            if size > 0 and size < minimum:
                minimum = size
    
    return minimum

def exploreIsland2(matrix, i, j, visited):
    rowInBound = i >= 0 and i < len(matrix)
    colInBound = j >= 0 and j < len(matrix[0])

    if not (rowInBound and colInBound):
        return 0
    
    if matrix[i][j] == 'w':
        return 0
    
    if (i, j) in visited:
        return 0
    
    visited.add((i, j))

    size = 1

    size += exploreIsland2(matrix, i + 1, j, visited)
    size += exploreIsland2(matrix, i - 1, j, visited)
    size += exploreIsland2(matrix, i, j + 1, visited)
    size += exploreIsland2(matrix, i, j - 1, visited)

    return size



print('Correct: ', minimum_island(grid))
print('Practice: ', minimum_island2(grid))
