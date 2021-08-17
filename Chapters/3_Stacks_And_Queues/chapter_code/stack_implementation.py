class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, input_data=None):
        self.top = None
        if input_data:
            for item in input_data:
                self.push(item)

    def push(self, value):
        new_node = StackNode(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        return_value = self.top.value
        self.top = self.top.next
        return return_value

    def __str__(self):
        return f"[{', '.join([str(value) for value in self])}]"

    def __iter__(self):
        return StackIterator(self)

class StackIterator:
    def __init__(self, stack):
        self.next = stack.top

    def __iter__(self):
        return self

    def __next__(self):
        if not self.next:
            raise StopIteration
        else:
            return_value = self.next.value
            self.next = self.next.next
            return return_value

print(Stack([1, 2, 3, 4, 123, 123, 123, 12318231]))