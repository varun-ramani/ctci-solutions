from typing import List

class MinBinaryHeap:
    def __init__(self, capacity=100):
        self.values: List = [None] * capacity
        self.next_index = 0

    def add_capacity(self, capacity=100):
        self.values.extend([None] * capacity)
    
    @staticmethod
    def compute_parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def compute_left_child_index(index):
        return (index * 2) + 1
    
    @staticmethod
    def compute_right_child_index(index):
        return (index * 2) + 2

    def add_value(self, value):
        if self.next_index == len(self.values):
            self.add_capacity()

        self.values[self.next_index] = value

        curr_node_index = self.next_index
        parent_node_index = MinBinaryHeap.compute_parent_index(curr_node_index)

        while curr_node_index != 0 and self.values[parent_node_index] > self.values[curr_node_index]:
            self.values[parent_node_index], self.values[curr_node_index] = self.values[curr_node_index], self.values[parent_node_index]
            curr_node_index = parent_node_index
            parent_node_index = MinBinaryHeap.compute_parent_index(curr_node_index) 

        self.next_index += 1
            
    def pop_root(self):
        if self.next_index == 0:
            return None

        return_value = self.values[0]
        self.values[0] = self.values[self.next_index - 1]
        self.values[self.next_index - 1] = None

        curr = 0
        left = MinBinaryHeap.compute_left_child_index(curr)
        right = MinBinaryHeap.compute_right_child_index(curr)
        
        while (self.values[left] is not None and self.values[left] < self.values[curr]
                or self.values[right] is not None and self.values[right] < self.values[curr]):
            if self.values[left] is not None and self.values[right] is not None:
                if self.values[left] < self.values[right]:
                    self.values[left], self.values[curr] = self.values[curr], self.values[left]
                    curr = left
                else:
                    self.values[right], self.values[curr] = self.values[curr], self.values[right]
                    curr = right

            elif self.values[right] is not None:
                self.values[right], self.values[curr] = self.values[curr], self.values[right]
                curr = right
            else:
                self.values[left], self.values[curr] = self.values[curr], self.values[left]
                curr = left
            
            left = MinBinaryHeap.compute_left_child_index(curr)
            right = MinBinaryHeap.compute_right_child_index(curr)

        self.next_index -= 1
        return return_value

    def is_empty(self):
        return self.next_index == 0

def heapsort(data):
    heap = MinBinaryHeap()
    for item in data:
        heap.add_value(item)
    
    while not heap.is_empty():
        print(heap.pop_root())

heapsort([5, 2, 3, 5])