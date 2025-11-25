from collections import deque
#[EASY] Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

#   1
#  / \
# 2   3
#    / \
#   4   5


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
b.left = None
b.right = None
c.left = d
c.right = e


def printNodes(root):
    if not root:
        return 
    
    result = []
    queue = deque([root])

    while queue:
        if root.left:
            current = queue.popleft()
            print(current.val, end=" ")
            result.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
    
    return result

print(printNodes(a))
