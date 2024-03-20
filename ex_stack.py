class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # 直接リストの真偽値を返す
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # リストの最後の要素を直接参照
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
list1 = [1, 2, 3, 4, 5]

# リストのアイテムをスタックにプッシュ
for i in list1:
    stack.push(i)

reversed_list = []

# スタックが空でない間、ポップしてリストに追加
while not stack.is_empty():
    # リストへのアイテムの追加方法を修正
    reversed_list.append(stack.pop())

print(reversed_list)
