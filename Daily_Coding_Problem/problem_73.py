#[EASY][SOLVED] Given the head of a singly linked list, reverse it in-place.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def reverse_list(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def print_linked_list(head):
    current = head

    while current != None:
        print(current.val)
        current = current.next

print_linked_list(reverse_list(a))




