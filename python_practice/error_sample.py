def get_book(index):
    books = ['Harry Potter', 'The Hobbit', 'The Lord of the Rings']
    try:
        return books[index]
    except IndexError:
        print('IndexErrorが発生しました')
        return 'リストの範囲外です'
    except TypeError:
        print('TypeErrorが発生しました')
S


if __name__ == '__main__':
    print(get_book(10))
    print(get_book('a'))
    print(get_book(2))
