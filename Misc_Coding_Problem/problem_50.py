#[EASY][SOLVED] Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#      *
#     / \
#    +    +
#   / \  / \
#  3  2  4  5

# You should return 45, as it is (3 + 2) * (4 + 5).

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a = Node('*')
b = Node('+')
c = Node('+')
d = Node(3)
e = Node(2)
f = Node(4)
g = Node(5)


a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

def solve_tree(root):
    if not root.left and not root.right:
        return root.value
    
    left = solve_tree(root.left)
    right = solve_tree(root.right)

    if root.value == '+':
        return left + right
    elif root.value == '-':
        return left - right
    elif root.value == '*':
        return left * right
    elif root.value == '/':
        return left / right
    
root = a
print(solve_tree(root))