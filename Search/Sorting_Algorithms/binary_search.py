
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

#binary search practice 2
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

def binary_search3(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = int((low + high) // 2)

        if numbers[middle] == target:
            return middle
        elif numbers[middle] > target:
            high = middle - 1
        elif numbers[middle] < target:
            low = middle + 1
    
    return -1
            

numbers = [2,3,5,6,7,8,23,45,65,101]
target1T = 45
target1F = 56

print('Correct/ True: ', binary_search(numbers, target1T))
print('Correc/ False: ', binary_search(numbers, target1F))

print('Practice/ True:', binary_search3(numbers, target1T))
print('Practice/ False: ', binary_search3(numbers, target1F))

