from student_card import StudentCard


class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        super().__init__(id, name)
        self.__nationality = nationality

    def get_nationality(self):
        return self.__nationality

    def print_info(self):
        super().print_info()
        print(f'国籍: {self.get_nationality()}')


if __name__ == '__main__':
    a = IStudentCard(1234, '鈴木一郎', '日本')
    a.print_info()
