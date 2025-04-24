import heapq
#[MEDIUM][SOLVED] Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(7)
e = Node(8)

a.next = b
b.next = c
c.next = d
d.next = e

e = Node(3)
f = Node(4)
g = Node(6)
h = Node(9)
i = Node(12)

e.next = f
f.next = g
g.next = h
h.next = i

j = Node(1)
k = Node(2)
l = Node(3)
m = Node(4)
n = Node(5)

j.next = k
k.next = l
l.next = m
m.next = n

def print_list(head):
    if not head:
        return []
    
    current = head
    result = []

    while current:
        result.append(current.val)
        current = current.next
    
    return result

def merge_lists(lists):
    heap = []

    for list in lists:
        if list:
            heapq.heappush(heap, list)
    
    dummy = Node(0)
    current = dummy

    while heap:
        smallest = heapq.heappop(heap)
        current.next = smallest
        current = current.next
        if smallest.next:
            heapq.heappush(heap, smallest.next)
    
    return dummy.next

lists = [a, j, e]
print(print_list(merge_lists(lists)))





    