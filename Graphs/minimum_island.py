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


print('Correct: ', minimum_island(grid))
