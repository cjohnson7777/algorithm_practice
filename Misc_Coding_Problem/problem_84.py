import timeit
import time
#[MEDIUM][SOLVED] Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

def count_islands(matrix):
    count = 0
    visited = set()
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and explore(matrix, i, j, visited) == True:
                count += 1
    
    return count

def count_islands2(matrix):
    count = 0
    visited = set()
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and explore(matrix, i, j, visited) == True:
                count += 1
    
    return count

def explore(matrix, i, j, visited):
    rowInBound = i >= 0 and i < len(matrix)
    colInBound = j >= 0 and j < len(matrix[0])

    if not (rowInBound and colInBound):
        return False
    
    if (i, j) in visited:
        return False
    
    if matrix[i][j] == 0:
        return False
    
    visited.add((i, j))

    explore(matrix, i - 1, j, visited)
    explore(matrix, i + 1, j, visited)
    explore(matrix, i, j - 1, visited)
    explore(matrix, i, j + 1, visited)

    return True

matrix = [  [1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]
        ]

start = time.perf_counter()
print(count_islands(matrix))
end = time.perf_counter()
time_taken = end - start
print(f"Time taken regular algorithm: {time_taken}")

start = time.perf_counter()
print(count_islands2(matrix))
end = time.perf_counter()
time_taken2 = end - start
print(f"Time taken other algorithm: {time_taken2}")
