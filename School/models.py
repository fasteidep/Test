from dataclasses import dataclass
from enum import Enum
class Chel:
    def __init__(
        self,
        name:str,
        last_name:str,
        age:int,
        ) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age

class StudSubj(Enum):
    MATH = 'math'
    GEOGRAPHY = 'geography'
    PE = 'pe'

class Student(Chel):
    def __init__(
        self,
        grades:dict[StudSubj, float],
        name:str,
        last_name:str,
        age:int
        ) -> None:
        super().__init__(name, last_name, age)
        self.grades = grades
        

@dataclass
class StudClass:
    name:str
    stud_list:list[Student]
    teacher:str



class Teacher(Chel):
    def __init__(self, name: str, last_name: str, age: int, class_assigned:StudClass) -> None:
        super().__init__(name, last_name, age)

class Menu:
    class_list = []

    def start_menu(self):
        while True:
            print('''
            ___Школа___
            Проект для лохов
            С мега функционалом
            Вот это да\n''')
            
            answ = input('''
            Чо ты хочешь сделат
            1 - Работа со школьными классами
            2 - Работа с ученками
            3 - Выход\n''')
            if answ=='1':
                self.class_menu()
            elif answ =='2':
                self.stud_menu()
            elif answ=='3':
                exit()
            
    def class_menu(self):
        print('''
        ___Работа с классами___
              ''')
        
        answ = input('''
        1 - Добавить класс
        2 - Добавить ученика
        3 - Добавить учителя
        4 - Просмотр всех людей\n''')
        
        if answ == '1':
            self.add_class()
        elif answ == '2':
            self.add_student()
        elif answ == '3':
            self.add_teacher()
        elif answ == '4':
            self.view_all_people()
        else:
            print('Неверный ввод')
            
    def stud_menu(self):
        print('''
        ___Работа с учениками___
            ''')
        
        answ = input('''
        1 - Добавить оценку ученику
        2 - Посмотреть оценки ученика\n''')
        if answ == '1':
            self.add_grade()
        elif answ == '2':
            self.view_grades()
        else:
            print('Неверный ввод')    
        
    
    def add_class(self):
        class_name = input('Введите добавляемый класс: ')
        added_class = StudClass(name=class_name, stud_list=[], teacher=None)
        self.class_list.append(added_class)
        print(f'{class_name} класс добавлен')
        
    def add_student(self):
        name = input('Введите имя ученика: ')
        last_name = input('Введите фамилию ученика: ')
        age = int(input('Введите возраст ученика: '))
        add_class = input('Введите, в какой класс его добавить: ')
        grades = {StudSubj.MATH: 0, StudSubj.GEOGRAPHY: 0, StudSubj.PE: 0}
        student = Student(name=name, last_name=last_name, age=age, grades=grades)
        for stud_class in self.class_list:
            if stud_class.name == add_class:
                stud_class.stud_list.append(student)
                print(f'Ученик {name} {last_name} добавлен в класс {add_class}')
                return
        print(f'Класс {add_class} не найден')
        
    def add_teacher(self):
        name = input('Введите имя учителя: ')
        last_name = input('Введите фамилию учителя: ')
        age = int(input('Введите возраст учителя: '))
        class_ = input('Введите, каким классом будет руководить учитель: ')
        for stud_class in self.class_list:
            if stud_class.name == class_:
                teacher = Teacher(name=name, last_name=last_name, age=age, class_assigned=stud_class)
                stud_class.teacher = teacher
                print(f'{teacher.name} {teacher.last_name} руководит {class_} классом')
                return
        print(f'{class_} класс не найден')
    
    def view_all_people(self):
        for class_ in self.class_list:
            print(f'{class_.name}: ')
            print(f'Учитель: {class_.teacher.name} {class_.teacher.last_name}, возраст - {class_.teacher.age}')
            
            for student in class_.stud_list:
                print(f'Ученик: {student.name} {student.last_name}, возраст - {student.age}')
    def add_grade(self):
        class_ = input('Введите класс ученика: ')
        name = input('Введите имя ученика: ')
        last_name = input('Введите фамилию ученика: ')
        for class__ in self.class_list:
            if class__.name == class_:
                for student in class__.stud_list:
                    if student.name == name and student.last_name == last_name:
                        subject = input('Введите предмет, по которому нужно поставить оценку (Math, GEOGRAPHY, PE): ')
                        Mark = float(input('Введите оценку (десятичной дробью): '))
                        student.grades[subject] = Mark
                        print(f'Оценка {Mark} по предмету {subject} успешно добавлена для ученика {student.name} {student.last_name}')
                        return
        print('Произошла ошибка')
        
    def view_grades(self):
        class_ = input('Введите класс ученика: ')
        name = input('Введите имя ученика: ')
        last_name = input('Введите фамилию ученика: ')
        for class__ in self.class_list:
            if class__.name == class_:
                for student in class__.stud_list:
                    if student.name == name and student.last_name == last_name:
                        for subject, grade in student.grades.items():
                            print(f'{subject}: {grade}')
                        return
        print('Произошла ошибка')



