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

print(tree_sum_breadth(n))

#your attempt
def tree_sum_depth(root):
    if not root:
        return 0
    sum = 0
    sum += root.value + tree_sum_depth(root.left) + tree_sum_depth(root.right)
    return sum

#print(tree_sum_depth(a))

#simplified attempt
def tree_sum(root):
    if not root:
        return 0
    
    return root.value + tree_sum(root.left) + tree_sum(root.right)


print("Correct: ", tree_sum(a))