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

#breadth first tree includes
def tree_includes_breadth(root, node):
    if not root:
        return False
    
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current.value == node:
            return True
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return False

#depth first recursive tree includes
def tree_includes_r(root, target):
    if not root:
        return False
    
    if root.value == target:
        return True
    
    return (tree_includes_r(root.left, target) or tree_includes_r(root.right, target))

#tree includes recursive practice 3
def tree_includes_r3(root, target):
    if not root:
        return False
    
    if root.value == target:
        return True
    
    return tree_includes_r3(root.left, target) or tree_includes_r3(root.right, target)



#print("Correct: ", tree_includes_breadth(a, 'q'))

print("Correct: ", tree_includes_r(a, 'b'))
print("Practice: ", tree_includes_r3(a, 'b'))

