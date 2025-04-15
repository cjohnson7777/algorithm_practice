from node_class import Node

a = Node(2)
b = Node(4)
c = Node(6)
d = Node(8)

a.next = b
b.next = c
c.next = d

head = [a, b, c, d]



def middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value


def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    curr = slow.next
    slow.next = None  # Split the list into two halves
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Merge two halves
    first, second = head, prev
    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2


