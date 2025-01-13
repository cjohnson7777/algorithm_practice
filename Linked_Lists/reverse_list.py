#Time O(n)
#Space O(1) - Iterative / O(n) - Recursive
from node_class import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

#reverse list iterative
def reverse_list(head):
    current = head
    prev = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current.next = next
    return prev
        

print(reverse_list(a))    