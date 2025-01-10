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
        return f"Person<{self._name} {self._surname} ({self._birthday})>"
    
class Student(Person):
    def __init__(self, name, lastname, birthday):
        super().__init__(name, lastname, birthday)
        self.lectures = {}

    def add_lecture(self, lecture, mark):
        self.lectures[lecture] = mark
    
    @property
    def grade_average(self):
        if not self.lectures:
            return 0
        return sum(self.lectures.values()) / len(self.lectures)

    def __repr__(self):
        return f"Student<{self._name} {self._surname} ({self._birthday})>"

class Worker(Person):
    def __init__(self, name, lastname, birthday, pay_per_hour):
        super().__init__(name, lastname, birthday)
        self.pay_per_hour = pay_per_hour
    
    @property
    def day_salary(self):
        return self.pay_per_hour * 8
    
    @property
    def month_salary(self):
        return self.day_salary * 30
    
    @property
    def year_salary(self):
        return self.month_salary * 12

    def __repr__(self):
        return f"Worker<{self._name} {self._surname} ({self._birthday})>"

class Wizard(Person):
    def __init__(self, name, lastname, birthday, power):
        super().__init__(name, lastname, birthday)
        self.age = power

    @property
    def age(self):
        return (datetime.now() - self._birthday).days

    @age.setter
    def age(self, days):
        self._birthday = datetime.now() - timedelta(days=days)
    
    def __repr__(self):
        return f"Wizard<{self._name} {self._surname} ({self._birthday})>"