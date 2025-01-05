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

#tree min stack iterative 
def tree_min_iterative(root):
    if not root:
        return None
    stack = [root]
    min = math.inf

    while stack:
        current = stack.pop()

        if current.value < min:
            min = current.value
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return min

        
#print(tree_min_iterative(a))

#tree minimun recusive
def tree_min(root):
    if not root:
        return math.inf
    
    return min(root.value, tree_min(root.left), tree_min(root.right))

print("Correct", tree_min(a))