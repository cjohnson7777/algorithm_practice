import math
from node_class import Node

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def max_path_root(root):
    if not root:
        return -math.inf
    
    if not (root.left and root.right):
        return root.value
    
    maxPath = max(max_path_root(root.left), max_path_root(root.right))
    
    return root.value + maxPath

print(max_path_root(a))