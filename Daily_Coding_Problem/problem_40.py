#[HARD] Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.
# NOT UNDERSTOOD

def appears_once(nums):
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones

nums = [6, 1, 3, 3, 3, 6, 6]

print(appears_once(nums))
print(appears_once([13, 19, 13, 13]))