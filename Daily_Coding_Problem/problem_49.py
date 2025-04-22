#[MEDIUM] Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.


def max_contiguous_sum(nums):
    current_max = 0
    global_max = 0

    for num in nums:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)

    return global_max

nums = [34, -50, 42, 14, -5, 86]
print(max_contiguous_sum(nums))

print(max_contiguous_sum([-5, -1, -8, -9]))
