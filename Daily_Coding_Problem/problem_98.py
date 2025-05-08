#[EASY] Given a 2D board of characters and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example, given the following board:

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.



# def exists(matrix, target):
#     visited = set()

#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             word = ""
#             if explore(matrix, i, j, target, word) == True:
#                 return True

#     return False

# def explore(matrix, i, j, target, word):
#     rowInBound = i >= 0 and i < len(matrix)
#     colInBound = j >= 0 and j < len(matrix[0])

#     if not (rowInBound and colInBound):
#         return False
    
#     if word == target:
#         return True
    
#     word += matrix[i][j]

#     explore(matrix, i - 1, j, target, word)
#     explore(matrix, i + 1, j, target, word)
#     explore(matrix, i, j - 1, target, word)
#     explore(matrix, i, j + 1, target, word)

#     return False


# board =  [
#             ['A','B','C','E'],
#             ['S','F','C','S'],
#             ['A','D','E','E'] 
#         ]

# print(exists(board, "ABCCED"))    
