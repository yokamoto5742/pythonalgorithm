def get_book_upper(index):
    books = ['Harry Potter', 'The Hobbit', 'The Lord of the Rings']
    try:
        book = str(books[index])
    except(IndexError, TypeError) as e:
        print(f'例外が発生しました:{e}')
    else:
        return book.upper()


if __name__ == '__main__':
    print(get_book_upper(10))
    print(get_book_upper('a'))
    print(get_book_upper(2))
