# ArrayList from scratch
class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = [None] * capacity
        self.next_index = 0
        
    def append(self, item):
        if self.next_index == self.capacity:
            self.capacity *= 2
            new_items = [None] * self.capacity