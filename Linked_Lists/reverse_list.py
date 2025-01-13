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

def print_linked_list(head):
    current = head

    while current != None:
        print(current.value)
        current = current.next

#reverse list iterative
def reverse_list(head):
    current = head
    prev = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

#reverse list recursive
def reverse_list_r(head, prev=None):
    if head == None:
        return prev
    
    next = head.next
    head.next = prev
    
    return(reverse_list_r(next, head))
    


print_linked_list(reverse_list(a))