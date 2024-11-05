
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

def matrix_binary_search(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top = 0
    bottom = ROWS - 1

    while top <= bottom:
        row = (top + bottom) // 2
        if target < matrix[row][0]:
            bottom = row - 1
        elif target > matrix[row][-1]:
            top = row + 1
        else:
            break
    
    if not (top <= bottom):
        return -1
    
    row = (top + bottom) // 2
    low = 0
    high = COLS - 1

    while low <= high:
        middle = (low + high) // 2
        if target < matrix[row][middle]:
            high = middle - 1
        elif target > matrix[row][middle]:
            low = middle + 1
        elif target == matrix[row][middle]:
            return row, middle
        
    return -1


    


numbers = [2,3,5,6,7,8,23,45,65,101]
matrix = [[1,2,4,5],[6,7,8,9],[10,11,12,13]]
target = 56

#print(binary_search2(numbers, target))
print(matrix_binary_search(matrix, target))