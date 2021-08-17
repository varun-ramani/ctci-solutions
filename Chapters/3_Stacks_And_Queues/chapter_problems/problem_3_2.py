class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class MinStack:
    def __init__(self):
        self.min_value = None
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

        if self.min_value is None or value < self.min_value:
            self.min_value = value

    def pop(self):
        if not self.top:
            return None

        return_value = self.top.value
        self.top = self.top.next
        return return_value

    def get_min(self):
        return self.min_value

stack = MinStack()
input_data = list(range(0, 100))

for index, item in enumerate(input_data):
    stack.push(item)

    min_data_value = min(input_data[:(index + 1)])
    stack_min = stack.get_min()
    if stack_min != min_data_value:
        print(f"Failed min test - on {index} expected {min_data_value} but got {stack_min}")

print("Minimum value function works")

for item in reversed(input_data):
    assert stack.pop() == item, "Stack doesn't reverse the input"
print("Stack reverses the input")