from datetime import datetime, timedelta

class Person:
    def __init__(self, name, lastname, birthday):
        self._name = name
        self._surname = lastname
        self._birthday = datetime.strptime(birthday, '%Y-%m-%d')

    def set_name(self, name):
        self._name = name
    
    def set_surname(self, surname):
        self._surname = surname
    
    def set_birthdate(self, birthday):
        self._birthday = datetime.strptime(birthday, '%Y-%m-%d')
    
    def get_name(self):
        return self._name
    
    def get_surname(self):
        return self._surname
    
    def get_birthday(self):
        return self._birthday.strftime('%Y-%m-%d')
    
    def __repr__(self):
        return f"Person<{self._name} {self._surname} ({self.get_birthday()})>"

class GradeDescriptor:
    def __get__(self, instance, owner):
        if not instance.lectures:
            return 0
        return sum(instance.lectures.values()) / len(instance.lectures)

class Student(Person):
    grade_average = GradeDescriptor()

    def __init__(self, name, lastname, birthday):
        super().__init__(name, lastname, birthday)
        self.lectures = {}

    def add_lecture(self, lecture, mark):
        self.lectures[lecture] = mark

    def __repr__(self):
        return f"Student<{self._name} {self._surname} ({self.get_birthday()})>"

class SalaryDescriptor:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.pay_per_hour * self.multiplier

class Worker(Person):
    day_salary = SalaryDescriptor(8)
    month_salary = SalaryDescriptor(8 * 30)
    year_salary = SalaryDescriptor(8 * 30 * 12)

    def __init__(self, name, lastname, birthday, pay_per_hour):
        super().__init__(name, lastname, birthday)
        self.pay_per_hour = pay_per_hour

    def __repr__(self):
        return f"Worker<{self._name} {self._surname} ({self.get_birthday()})>"

class AgeDescriptor:
    def __get__(self, instance, owner):
        return (datetime.now() - instance._birthday).days

    def __set__(self, instance, days):
        instance._birthday = datetime.now() - timedelta(days=days)

class Wizard(Person):
    age = AgeDescriptor()

    def __init__(self, name, lastname, birthday):
        super().__init__(name, lastname, birthday)

    def __repr__(self):
        return f"Wizard<{self._name} {self._surname} ({self.get_birthday()})>"