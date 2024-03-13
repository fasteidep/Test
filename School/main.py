from models import Chel, StudSubj, Student, StudClass, Teacher

class_a = StudClass('101А', stud_list=[])
teachers = []

while True:
    answ = input('1 - Добавить ученика в класс\n'
                 '2 - Добавить учителя\n'
                 '3 - Посмотреть всех людей\n'
                )

    if answ == '1':
        name = input('Введите имя ученика: ')
        last_name = input('Введите фамилию ученика: ')
        age = int(input('Введите возраст ученика: '))
        student = Student(grades={StudSubj.MATH: 0, StudSubj.GEOGRAPHY: 0, StudSubj.PE: 0}, name=name, last_name=last_name, age=age)
        class_a.stud_list.append(student)
        print(f'Ученик {name} {last_name} добавлен в класс {class_a.name}')
    elif answ == '2':
        name = input('Введите имя учителя: ')
        last_name = input('Введите фамилию учителя: ')
        age = int(input('Введите возраст учителя: '))
        class_num = input('Введите класс учителя: ')
        teacher = Teacher(name, last_name, age, class_num)
        teachers.append(teacher)
        print(f'Учитель {name} {last_name} добавлен в базу')
    elif answ == '3':
        print(f'Список учеников в классе {class_a.name}:')
        for student in class_a.stud_list:
            print(student.name, student.last_name)
        print('\nСписок учителей:')
        for teacher in teachers:
            print(teacher.name, teacher.last_name, teacher.class_)

