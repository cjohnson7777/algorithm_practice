#[MEDIUM][SOLVED] Invert a binary tree.

# For example, given the following tree:

#     a
#    / \
#   b   c
#  / \  /
# d   e f
# should become:

#   a
#  / \
#  c  b
#  \  / \
#   f e  d

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

g = Node('a')
h = Node('b')
i = Node('c')
j = Node('d')
k = Node('e')
l = Node('f')

g.left = h
g.right = i
h.left = j
h.right = k
i.right = l


def invert_tree_q(root):
    queue = [root]

    while queue:
        current = queue.pop(0)
        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    
    return root

def invert_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root

def print_tree(root):
    if not root:
        return []
    
    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

print(print_tree(a))
print(print_tree(invert_tree_q(a)))
print(print_tree(invert_tree(g)))