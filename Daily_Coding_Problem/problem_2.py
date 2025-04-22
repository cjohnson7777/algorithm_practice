#[HARD] Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def product_except_self(nums):
    products = [1] * len(nums)
    pre = 1
    post = 1

    for i in range(len(nums)):
        products[i] = pre
        pre *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
        products[i] *= post
        post *= nums[i]
    
    return products

nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))