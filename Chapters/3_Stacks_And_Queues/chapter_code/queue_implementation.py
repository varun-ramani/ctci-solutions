class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.back = None

    def enqueue(self, value):
        new_node = QueueNode(value)

        if not self.front:
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = self.back.next

    def dequeue(self):
        if not self.front:
            return None

        return_value = self.front.value
        self.front = self.front.next

        if not self.front:
            self.back = None

        return return_value

    def peek(self):
        return self.front.value if self.front else None

    def is_empty(self):
        return False if self.front else True
    
    def __iter__(self):
        return QueueIterator(self)

    def __str__(self):
        return f"[{', '.join(str(value) for value in self)}]"

class QueueIterator:
    def __init__(self, queue):
        self.next_node = queue.front

    def __iter__(self):
        return self

    def __next__(self):
        if not self.next_node:
            raise StopIteration
        else:
            return_value = self.next_node.value
            self.next_node = self.next_node.next
            return return_value

my_queue = Queue()

for element in [1, 2, 3, 4]:
    my_queue.enqueue(element)

print(my_queue)

while not my_queue.is_empty():
    print(my_queue.dequeue())

print(my_queue)