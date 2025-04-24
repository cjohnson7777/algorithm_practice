#[MEDIUM][SOLVED] There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


def grid_traveler(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        return 0
    
    if m == 1 and n == 1:
        return 1
    
    memo[(m, n)] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1) 
    
    return memo[(m, n)]

print(grid_traveler(5, 5))