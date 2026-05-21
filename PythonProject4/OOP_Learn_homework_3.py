class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _get_avg_grade(self):
        """Вспомогательный метод для подсчета средней оценки за ДЗ"""
        if not self.grades:
            return 0.0
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        courses_in_progress_str = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет"

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._get_avg_grade():.1f}\n"
                f"Курсы in процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() < other._get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() > other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_grade() == other._get_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_avg_grade(self):
        """Вспомогательный метод для подсчета средней оценки за лекции"""
        if not self.grades:
            return 0.0
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self._get_avg_grade():.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() < other._get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() > other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_grade() == other._get_avg_grade()


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"