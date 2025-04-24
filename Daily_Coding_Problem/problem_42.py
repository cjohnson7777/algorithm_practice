#[HARD][NOT SOLVED] Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.


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

print(how_sum(24, [12, 1, 61, 5, 9, 2]))

    
