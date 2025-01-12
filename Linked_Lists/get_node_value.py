#Time: O(n)
#Space: O(1) - Iterative / O(n) - Recursive

from node_class import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

#get node value recursive
def get_node_value(head, index):
    return