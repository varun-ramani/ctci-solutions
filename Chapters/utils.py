class ListNodeIterator:
    def __init__(self, head):
        self.next_node = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_node is None:
            raise StopIteration
        else:
            return_value = self.next_node.val
            self.next_node = self.next_node.next
            return return_value

    def __str__(self):
        return f"[{', '.join([str(value) for value in self])}]"

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __iter__(self):
        return ListNodeIterator(self)

    def __repr__(self):
        return f"<ListNode val={self.val}>"

    def __str__(self):
        return str(self.val)

def build_ll(input):
    head = None
    current_node = None

    for item in input:
        new_node = ListNode(item)

        if head is None:
            head = current_node = new_node
        else:
            current_node.next = new_node
            current_node = current_node.next

    return head