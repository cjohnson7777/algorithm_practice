
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle
        elif arr[middle] < target:
            low = middle
    return -1


numbers = [2,3,5,6,7,8,23,45,65,101]
target = 2

print(binary_search(numbers, target))