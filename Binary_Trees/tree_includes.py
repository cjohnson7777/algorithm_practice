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

#recursive depth first tree includes
def tree_includes_depth(root, target):
    if not root:
        return False
    
    if root.value == target:
        return True
    
    return (tree_includes_depth(root.left, target) or tree_includes_depth(root.right, target))

#tree includes recursive 2
def tree_includes2(root, target):
    if not root:
        return False
    
    if root.value == target:
        return True
    
    return(tree_includes2(root.left, target) or tree_includes2(root.right, target))
    


#print("Correct: ", tree_includes_breadth(a, 'q'))

print("Correct: ", tree_includes_depth(a, 'b'))
print("Practice: ", tree_includes2(a, 'b'))

