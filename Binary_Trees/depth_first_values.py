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

n = None

#depth first tranversal iteratively
def depth_first_values(root):
    if not root:
        return []
    
    stack = [root]
    results = []

    while stack:
        current = stack.pop()
        results.append(current.value)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return results

#depth first traversal recursively
def depth_first_values_recursive(root):
    if not root:
        return None
    print(root.value)

    if root.left:
        depth_first_values_recursive(root.left)
    if root.right:
        depth_first_values_recursive(root.right)

#depth first traversal recursively (simple)
def depth_first_values_simple(root):
    if not root:
        return []
    
    leftValues = depth_first_values_simple(root.left)
    rightValues = depth_first_values_simple(root.right)

    return [root.value, *leftValues, *rightValues]


#depth first search recursively practice 2
def depth_first_values_recursive2(root):
    if not root:
        return None
    
    print(root.value)
    
    if root.left:
        depth_first_values_recursive2(root.left)
    if root.right:
        depth_first_values_recursive2(root.right)

#depth first practice simple 3
def depth_first_values_simple3(root):
    if not root:
        return []
    
    leftValues = depth_first_values_simple3(root.left)
    rightValues = depth_first_values_simple3(root.right)

    return [root.value, *leftValues, *rightValues]



#print("Iterative: ", depth_first_values(n))

print("\t Correct")
depth_first_values_recursive(a)
print("\t Practice")
print(depth_first_values_simple3(a))
# print("Correct (simple): ", depth_first_values_simple(a))
# print("Practice (simple): ", depth_first_values_simple3(a))