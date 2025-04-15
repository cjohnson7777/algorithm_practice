# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.


def first_missing_int(nums):
    n = len(nums)
    for i in range(len(nums)):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
        
    return n + 1

nums = [3, 4, -1, 1]
print(first_missing_int(nums))

