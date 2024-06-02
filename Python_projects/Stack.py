class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display(self):
        print("stack:", self.items)

# Create a Stack instance and perform operations
s = Stack()
s.push(1)
s.push(2)
s.display()

pop_element = s.pop()
print("popped element:", pop_element)
s.display()

t_item = s.peek()
print("top item:", t_item)
