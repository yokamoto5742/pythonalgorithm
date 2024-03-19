def first_item(items):
    if items:
        return items[0]
    else:
        return None


if __name__ == '__main__':
    print(first_item(['book']))
    print(first_item([]))
