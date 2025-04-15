import bisect
#[HARD] Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
# NOT UNDERSTOOD



def longest_subsequence_dp(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] <nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)


def longest_subsequence(nums):
    subsequence = []

    for num in nums:
        i = bisect.bisect_left(subsequence, num)
        if i == len(subsequence):
            subsequence.append(num)
        else:
            subsequence[i] = num
    
    return len(subsequence)
 
nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_subsequence_dp(nums))
