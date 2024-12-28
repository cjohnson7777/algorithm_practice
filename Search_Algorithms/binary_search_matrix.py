
#binary search matrix
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
            return True, row, middle
        
    return -1

#matrix_binary_search2
def matrix_binary_search2(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top = 0
    bottom = ROWS - 1

    while top <= bottom: 
        row = int((top + bottom) // 2)
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    
    if not top <= bottom:
        return -1
    
    low = 0
    high = COLS - 1
    row = (top + bottom) // 2

    while low <= high:
        middle = int((low + high) // 2)
        if target == matrix[row][middle]:
            return True, row, middle
        elif target > matrix[row][middle]:
            low = middle + 1
        elif target < matrix[row][middle]:
            high = middle - 1
    
    return -1
    


matrix = [[1,2,4,5],[6,7,8,9],[10,11,12,13]]
target = 10
print('Correct: ', matrix_binary_search(matrix, target))
print('Practice: ', matrix_binary_search2(matrix, target))