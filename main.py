from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.li = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_le(self, lecturer, course, le_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.le_grade:
                lecturer.le_grade[course] += [le_grade]
            else:
                lecturer.le_grade[course] = [le_grade]
        else:
            return 'Ошибка'

    def avr(self):
        av_g = []
        for key, value in self.grades.items():
            av_g.append(mean(value))
        return mean(av_g)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за предмет: {self.avr()}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}'

        return res




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.le_grade = {}

    def avg(self):
        av_g = []
        for value in self.le_grade.values():
            av_g.append(mean(value))
        return mean(av_g)


    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за лекции: {self.avg()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
student_1 = Student('Eliot', 'Mann', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_2 = Student('Alex', 'Moor', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
Reviewer_1 = Reviewer('Лев', 'Иванов')
Reviewer_1.courses_attached += ['Python']
Reviewer_1.courses_attached += ['Git']
Reviewer_2 = Reviewer('Иван', 'Петров')
Reviewer_2.courses_attached += ['Python']
Reviewer_2.courses_attached += ['Git']

cool_Reviewer.rate_hw(best_student, 'Python', 10)
Reviewer_1.rate_hw(student_1, 'Python', 2)
Reviewer_2.rate_hw(student_2, 'Python', 5)
Reviewer_2.rate_hw(student_2, 'Git', 9)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
lecturer_1 = Lecturer('Олег', 'Бубнов')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
lecturer_2 = Lecturer('Глеб', 'Афанасьев')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

best_student.rate_le(cool_lecturer, 'Python', 8)
student_1.rate_le(lecturer_1, 'Python', 10)
student_2.rate_le(lecturer_2, 'Python', 9)
best_student.rate_le(cool_lecturer, 'Git', 1)
student_1.rate_le(lecturer_1, 'Git', 2)
student_2.rate_le(lecturer_2, 'Git', 3)

# print('Лекторы')
# print(cool_lecturer)
# print(lecturer_1)
# print(lecturer_2)
# print()
# print('Ревьюеры')
# print(cool_Reviewer)
# print(Reviewer_1)
# print(Reviewer_2)
# print('Студенты')
# print()
print(best_student)
print(student_1)
print(student_2)

