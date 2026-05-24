# Задание 4
from OOP_Learn_homework_3 import Student, Lecturer, Reviewer

# Создаем по 2 экземпляра каждого класса

# Студенты
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jane', 'Doe', 'female')
student_2.courses_in_progress += ['Python', 'Django']
student_2.finished_courses += ['Основы логики']

# Лекторы
lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('John', 'Smith')
lecturer_2.courses_attached += ['Python', 'Django']

# Эксперты (Reviewers)
reviewer_1 = Reviewer('Alan', 'Turing')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Grace', 'Hopper')
reviewer_2.courses_attached += ['Python', 'Django']

# Вызываем все созданные методы (тестируем логику)

# Ревьюеры выставляют оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 8)

reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Django', 10)

# Студенты выставляют оценки лекторам
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Git', 10)

student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Django', 10)

# Проверяем вывод (магические методы __str__)
print("=== СТУДЕНТЫ ===")
print(student_1)
print("-" * 20)
print(student_2)

print("\n=== ЛЕКТОРЫ ===")
print(lecturer_1)
print("-" * 20)
print(lecturer_2)

print("\n=== ЭКСПЕРТЫ (Reviewers) ===")
print(reviewer_1)
print("-" * 20)
print(reviewer_2)

# Проверяем сравнение (магические методы __lt__, __gt__, __eq__)
print("\n=== СРАВНЕНИЕ ===")
print(f"Студент {student_1.name} учится лучше {student_2.name}? -> {student_1 > student_2}")
print(f"Лектор {lecturer_1.name} преподает хуже {lecturer_2.name}? -> {lecturer_1 < lecturer_2}")

# Реализуем две функции

def get_avg_hw_grade_by_course(students_list, course_name):
    """Подсчет средней оценки за домашние задания по всем студентам в рамках курса"""
    total_sum = 0
    total_count = 0

    for student in students_list:
        if course_name in student.grades:
            total_sum += sum(student.grades[course_name])
            total_count += len(student.grades[course_name])

    if total_count == 0:
        return 0.0
    return round(total_sum / total_count, 1)


def get_avg_lecture_grade_by_course(lecturers_list, course_name):
    """Подсчет средней оценки за лекции всех лекторов в рамках курса"""
    total_sum = 0
    total_count = 0

    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total_sum += sum(lecturer.grades[course_name])
            total_count += len(lecturer.grades[course_name])

    if total_count == 0:
        return 0.0
    return round(total_sum / total_count, 1)


# Проверяем работу функций
students_group = [student_1, student_2]
lecturers_group = [lecturer_1, lecturer_2]

print("\n=== АНАЛИТИКА ПО КУРСАМ ===")
print(f"Средняя оценка студентов по курсу 'Python': {get_avg_hw_grade_by_course(students_group, 'Python')}")
print(f"Средняя оценка студентов по курсу 'Git': {get_avg_hw_grade_by_course(students_group, 'Git')}")

print(f"Средняя оценка лекторов по курсу 'Python': {get_avg_lecture_grade_by_course(lecturers_group, 'Python')}")
print(f"Средняя оценка лекторов по курсу 'Django': {get_avg_lecture_grade_by_course(lecturers_group, 'Django')}")