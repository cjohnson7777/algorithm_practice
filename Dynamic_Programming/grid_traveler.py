
# my attempt
# O(2^n+m) time / O(n+m) space
def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    
    if m == 1 and n == 1:
        return 1
    
    count = 0

    count += grid_traveler(m - 1, n) 
    count += grid_traveler(m, n - 1)

    return count

# cleaner code
def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    
    if m == 1 and n == 1:
        return 1
    
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

# my memoized answer attempt
# O(n*m) time / O(n+m) space
def grid_traveler(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        return 0
    
    if m == 1 and n == 1:
        return 1
    
    memo[(m, n)] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1) 
    
    return memo[(m, n)]

#default arguments are evaluated at the first call, so the same default value is being used

# optimized memoized answer
# def grid_traveler(m, n, memo={}):
#     if (m, n) in memo in memo:
#         return memo[(m, n)]

#     if m == 0 or n == 0:
#         return 0
    
#     if m == 1 and n == 1:
#         return 1
    
#     memo[(m, n)], memo[(n, m)] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

    

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))

