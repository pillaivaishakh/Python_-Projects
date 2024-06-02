class Queue:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


    def size(self):
        return len(self.items)


    def display(self):
        print("Queue:", self.items)




# Create a queue object
queue = Queue()


# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)


# Display the queue
queue.display()  # Output: Queue: [10, 20, 30]


# Dequeue an element
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # Output: Dequeued item: 10


# Display the updated queue
queue.display()  # Output: Queue: [20, 30]
