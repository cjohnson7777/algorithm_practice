#[EASY] Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.


def word_search(matrix, word):

    for r in range(len(matrix)):
        search = ""
        for c in range(len(matrix)):
            search += matrix[r][c]
            if search == word:
                return True
    
    for r in range(len(matrix)):
        search = ""
        for c in range(len(matrix)):
            search += matrix[c][r]
            if search == word:
                return True


matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

target = 'FOAM'

print(word_search(matrix, target))
