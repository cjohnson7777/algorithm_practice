from node_class import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

#print linked list values iteratively
def print_linked_list(head):
    current = head

    while current != None:
        print(current.value)
        current = current.next

#print linked list recursively
def print_linked_list_r(head):
    if head == None:
        return
    
    print(head.value)
    print_linked_list_r(head.next)

#print linked list recusively in reverse
def print_linked_list_r_r(head):
    if head == None:
        return
    
    print_linked_list_r(head.next)
    print(head.value)

    
print_linked_list(a)
print()
print_linked_list_r(a)