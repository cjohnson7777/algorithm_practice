# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def two_sum(nums, k):
    seen = set()

    for num in nums:
        pair = k - num
        if pair in seen:
            return True
        seen.add(num)
    
    return False

def two_sum2(nums, k):
    seen = set(nums)

    for num in nums:
        if (k - num) in seen:
            return True
        
    return False


a = [10, 15, 3, 7]
k = 17
print(two_sum2(a, k))
    