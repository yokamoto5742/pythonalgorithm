class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.is_empty())

for i in range(10):
    q.enqueue(i)

print(q.items)

while not q.is_empty():
    print(q.dequeue(), end=' ')
