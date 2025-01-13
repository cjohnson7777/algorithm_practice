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
    if head == None:
        return None
    
    if index == 0:
        return head.value
    
    return get_node_value(head.next, index - 1)

#get node value iterative increment downwards
# def get_node_value_i(head, index):
#     current = head

#     while current != None:
#         if index == 0:
#             return current.value
#         index -= 1
#         current = current.next
#     return None

#get node value incrementing upwards
def get_node_value_i(head, index):
    current = head
    count  = 0

    while current != None:
        if count == index:
            return current.value
        count += 1
        current = current.next
    return None
    

print(get_node_value(a, 2))
print(get_node_value_i(a, 2))