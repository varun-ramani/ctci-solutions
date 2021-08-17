from .linked_list import SinglyLinkedList

# Iterate through the list with two pointers, moving at different rates.

# Deleting the n-th element from the end of the list
def DeleteNthElement(linked_list: SinglyLinkedList, n):
    pointer_1 = linked_list.head
    if pointer_1 is None:
        return

    for step in range(n):
        assert pointer_1, "Insufficient elements in linked list"
        pointer_1 = pointer_1.next

    if pointer_1 is None:
        linked_list.head = linked_list.head.next

    pointer_2 = linked_list.head
    while pointer_1.next is not None:
        pointer_2 = pointer_2.next
        pointer_1 = pointer_1.next

    pointer_2.next = None