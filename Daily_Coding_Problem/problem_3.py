#[MEDUIM] Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

#The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

#NEVER COMPLETED

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


def serialize(root):
    """Encodes a tree to a single string using preorder traversal."""
    def helper(node):
        if not node:
            return "None, "
        return str(node.val) + "," + helper(node.left) + helper(node.right)

    return helper(root)

def deserialize(data):
    """Decodes the encoded data to reconstruct the tree."""
    def helper(nodes):
        val = nodes.pop(0)
        if val == "None":
            return None
        node = Node(val)
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    node_list = data.split(",")
    return helper(node_list)

# def helper(nodes):
#     val = nodes.pop(0)
#     if val == "None":
#         return None
#     node = Node(val)
#     node.left = helper(nodes)
#     node.right = helper(nodes)
#     return node

list = serialize(a)
print(deserialize(list))

