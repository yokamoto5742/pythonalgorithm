class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()

for i in "こんにちは":
    stack.push(i)

reversed_string = ""

while not stack.is_empty():
    reversed_string += stack.pop()

print(reversed_string)
