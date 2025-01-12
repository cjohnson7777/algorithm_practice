#Time O(n)
#Space O(1) - Iterative /  O(n) - Recursive
from node_class import Node

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

#19

#sum list iterative
def sum_list(head):
    sum = 0
    current = head

    while current != None:
        sum += current.value
        current = current.next
    return sum

#sum list recursive
def sum_list_r(head):
    if head == None:
        return 0
    
    return head.value + sum_list_r(head.next)

print(sum_list(a))
print(sum_list_r(a))