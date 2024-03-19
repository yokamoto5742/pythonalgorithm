class StudentCard:
    school_name = '富山国際高等専門学校'

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def print_info(self):
        print(
            f'{self.school_name}\n学籍番号: {self.__id}\n氏名: {self.__name}'
        )


if __name__ == '__main__':
    a = StudentCard(1234, '鈴木一郎')
    a.print_info()
