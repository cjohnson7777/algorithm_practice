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


n = None

#tree sum breadth first
def tree_sum_breadth(root):
    sum = 0

    if not root: 
        return sum
    
    queue = [root]

    while queue:
        current = queue.pop(0)
        sum += current.value

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return sum

#tree sum breath practice 
def tree_sum_b2(root):
    if not root:
        return 0
    
    queue = [root]
    sum = 0

    while queue:
        current = queue.pop(0)
        sum += current.value

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return sum

#tree sum recusive
def tree_sum(root):
    if not root:
        return 0
    
    return root.value + tree_sum(root.left) + tree_sum(root.right)

#tree sum recursive practice 
def tree_sum3(root):
    if not root:
        return 0
    
    return root.value + tree_sum3(root.left) + tree_sum3(root.right)



print("Correct Breadth:", tree_sum_breadth(a))
print("Practice Breath: ", tree_sum_b2(a))

print("Correct: ", tree_sum(a))
print("Practice: ", tree_sum3(a))


