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

#tree min stack iterative practice 
def tree_min_i_2(root):
    if not root:
        return None
    
    min = math.inf
    stack = [root]

    while stack:
        current = stack.pop()

        if current.value < min:
            min = current.value
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    return min
            

#tree min recusive
def tree_min(root):
    if not root:
        return math.inf
    
    return min(root.value, tree_min(root.left), tree_min(root.right))


#tree min recursive practice 
def tree_min3(root):
    if not root:
        return math.inf
    
    return min(root.value, tree_min3(root.left), tree_min3(root.right))
    


print("Correct Iterative: ", tree_min_iterative(a))
print("Practice Iterative: ", tree_min_i_2(a))


print("Correct Recursive: ", tree_min(a))
print("Practice Recursive: ", tree_min3(a))