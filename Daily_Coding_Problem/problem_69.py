#[EASY] Given a list of integers, return the largest product that can be made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

# You can assume the list has at least three integers.


def max_product(arr):
    arr.sort()

    n = len(arr)
    return max(arr[n - 1] * arr[n - 2] * arr[n - 3], (arr[0] * arr[1]) * arr[n - 1])
   
    
arr = [-10, -10, 5, 2]
print(max_product(arr))