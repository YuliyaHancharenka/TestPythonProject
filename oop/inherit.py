class SchoolMember:
    '''Представляет любого человека в школе.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()  # печатает пустую строку

members = [t, s]
for member in members:
    member.tell()  # работает как для преподавателя, так и для студента

# Python не вызывает конструктор базового класса автоматически – его необходимо вызывать
# самостоятельно в явном виде.


# Заметьте также, что вызывается метод tell из подкласса, а не метод tell из
# класса SchoolMember. Это можно понять следующим образом: Python всегда на-
# чинает поиск методов в самом классе, что он и делает в данном случае. Если
# же он не находит метода, он начинает искать методы, принадлежащие базо-
# вым классам по очереди, в порядке, в котором они перечислены в кортеже при
# определении класса.

# Замечание по терминологии: если при наследовании перечислено более од-
# ного класса, это называется множественным наследованием.

# Параметр end используется в методе tell() для того, чтобы новая строка на-
# чиналась через пробел после вызова print().