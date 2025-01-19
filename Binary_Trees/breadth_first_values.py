#Time: O(n)
#Space: O(n)
import queue
from node_class import Node

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

#breadth first values
def breadth_first_values(root):
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

#breadth first values practice 3
def breadth_first_values_3(root):
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
        


print("Correct: ", breadth_first_values(a))
print("Practice:", breadth_first_values_3(a))