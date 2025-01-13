#Time O(min(n,m))
#Space O(1) - Iterative

from node_class import Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')

e.next = f
f.next = g
g.next = h
h.next = i

def print_linked_list(head):
    current = head

    while current != None:
        print(current.value)
        current = current.next

#zipper list iterative
def zipper_list(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 != None and current2 != None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        tail = tail.next
        count += 1
    
    if current1 != None:
        tail.next = current1
    if current2 != None:
        tail.next = current2
    
    return head1

#zipper list recursive
def zipper_list_r(head1, head2):
    if head1 == None and head2 == None:
        return None
    
    if head1 == None:
        return head2
    
    if head2 == None:
        return head2
    
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_list_r(next1, next2)

    return head1

print_linked_list(zipper_list(a, e))

