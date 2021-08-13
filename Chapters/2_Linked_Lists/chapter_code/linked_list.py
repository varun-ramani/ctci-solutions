class ListIterator:
    def __init__(self, head_node):
        self.current_node = head_node 

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        else:
            return_value = self.current_node.val
            self.current_node = self.current_node.next
            return return_value

class SingleLinkedNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, val):
        new_node = SingleLinkedNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            return_value = self.head.val
            self.head = self.tail = None
        else:
            return_value = self.tail.val

            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node

        self.length -= 1
        return return_value

    def __len__(self):
        return self.length

    def __iter__(self):
        return ListIterator(self.head)

    def __str__(self):
        return f"[{', '.join(self)}]"

my_list = SinglyLinkedList()

my_list.append("1")
my_list.append("2")
print(my_list)

print(my_list.pop(), my_list.pop())

print(my_list)

my_list.append("a")
my_list.append('2')
my_list.append("c")
print(my_list)