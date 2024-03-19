class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'氏名: {self.name}\n年齢: {self.age}')

    def age_check(self, i):
        return self.age > i

    @staticmethod
    def print_younger_person_name(p1, p2):
        if p1.age <= p2.age:
            print(p1.name)
        else:
            print(p2.name)

    @staticmethod
    def get_total_age(p1, p2):
        return p1.age + p2.age


if __name__ == '__main__':
    p1 = Person('太郎', 20)
    p2 = Person('花子', 18)
    p1.print_info()
    p2.print_info()
    Person.print_younger_person_name(p1, p2)
    print(Person.get_total_age(p1, p2))
