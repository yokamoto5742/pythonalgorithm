def list_books1(items):
    for item in items:
        if 'book' not in item:
            continue
        print(item)


def list_books2(items):
    copied_items = items.copy()
    while copied_items:
        item = copied_items.pop()
        if 'pen' not in item:
            continue
        print(item)


if __name__ == '__main__':
    items = ['book1', 'book2', 'pen1', 'pen2']
    list_books1(items)
    list_books2(items)
