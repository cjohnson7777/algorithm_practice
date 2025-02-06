
# Time O(n*m^2)
#Space O(m^2)

def how_sum(target, numbers, memo=None):
    if memo == None:
        memo = {}
    
    if target in memo:
        return memo[target]
    
    if target < 0:
        return None
    
    if target == 0:
        return []
    
    for num in numbers:
        result = how_sum(target - num, numbers, memo)
        if result != None:
            memo[target] = [num, *result]
            return memo[target]
        
    memo[target] = None
    return None

        
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 3]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14, 100]))

