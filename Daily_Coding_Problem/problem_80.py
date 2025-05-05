#[EASY][SOLVED] Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

#     a
#    / \
#   b   c
#  /
# d   

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.left = b
a.right = c
b.left = d

def deepest_node(root):
    if not root:
        return None
    
    stack = [root]

    while stack:
        current = stack.pop()

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return current.value

print(deepest_node(a))