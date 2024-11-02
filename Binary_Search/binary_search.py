
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = int((low + high) // 2)
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1
    return -1


def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = int((low + high) // 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            low = middle + 1
        elif nums[middle] > target:
            high = middle - 1
    return -1

def binary_search2(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = int((low + high) // 2)
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1
    return -1



numbers = [2,3,5,6,7,8,23,45,65,101]
target = 90

print(binary_search2(numbers, target))