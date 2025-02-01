
# # my first attempt
# def can_sum(target, nums):
#     if target == 0:
#         return True
    
#     for num in nums:
#         if target - num < 0:
#             continue
#         if can_sum(target - num, nums) == True:
#             return True
    
#     return False

# #Time O(n^m)
# #Space O(m)
# #second attempt
# def can_sum(target, nums):
#     if target == 0:
#         return True
    
#     if target < 0:
#         return False
    
#     for num in nums:
#         if can_sum(target - num, nums) == True:
#             return True
    
#     return False

#Time O(n*m)
#Space O(m)
#memoized attempt
def can_sum(target, nums, memo={}):
    if target in memo:
        return memo[target]
    
    if target == 0:
        return True
    
    if target < 0:
        return False
            
    for num in nums:
        if can_sum(target - num, nums) == True:
            memo[target] = True
            return True
        
    memo[target] = False
    return False


print(can_sum(7, [2, 4]))

print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 3]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))




    
