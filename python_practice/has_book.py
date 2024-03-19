def has_book1(items):
    for item in items:
        if 'book' in item:
            print('bookは見つかりました')
        else:
            print('bookは見つかりませんでした')


def has_book2(items):
    copy_items = items.copy()
    while copy_items:
        item = copy_items.pop()
        if 'book' in item:
            print('bookは見つかりました')
        else:
            print('bookは見つかりませんでした')


if __name__ == '__main__':
    has_book1(['note'])
    has_book1(['note', 'bookend'])
    has_book2(['note'])
    has_book2(['note', 'bookend'])
