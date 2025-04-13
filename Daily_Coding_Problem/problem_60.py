#[MEDIUM] Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

# NEEDS REVIEW

def can_partition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False
    
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True

    return dp[target]

nums = [15, 5, 20, 10, 35, 15, 10]
print(can_partition(nums))

print(can_partition([7, 10, 3, 2, 4]))
    


    