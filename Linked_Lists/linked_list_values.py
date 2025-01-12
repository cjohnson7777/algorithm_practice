#Time: O(n)
#Space: O(n)
from node_class import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

#linked list values iteravtive
def linked_list_values(head):
    current = head
    values = []

    while current != None:
        values.append(current.value)
        current = current.next
    return values

#linked list values recursively
def linked_list_values_r(head):
    values = []
    fill_values(head, values)
    
    return values

def fill_values(head, values):
    if head == None:
        return 
    
    values.append(head.value)
    fill_values(head.next, values)


print(linked_list_values(a))
print()
print(linked_list_values_r(a))