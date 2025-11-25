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

#linked list find iterative
def linked_list_find(head, target):
    # if isinstance(target, str):
    #     target = target.upper()
    current = head

    while current != None:
        if current.value == target:
            return True
        current = current.next
    
    return False

#linked list find recursive
def linked_list_find_r(head, target):
    if head == None:
        return False
    
    if head.value == target:
        return True
    
    return linked_list_find_r(head.next, target)

#linked list find recursive practice 
def linked_list_find_r2(head, target):
    if not head:
        return False
    
    if head.value == target:
        return True
    
    return linked_list_find_r2(head.next, target)

#linked list find iterative practice 
def linked_list_find_i2(head, target):
    if not head:
        return False
    
    current = head

    while current != None:
        if current.value == target:
            return True
        
        current = current.next
    
    return False


print("Correct: ")
print(linked_list_find(a, 'C'))
print(linked_list_find_r(a, 'C'))
print("Practice: ")
print(linked_list_find_r2(a, 'C'))
print(linked_list_find_i2(a, 'C'))