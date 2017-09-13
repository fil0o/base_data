"""Альтернативные реализации классов Person и Manager с данными, методами
и с перезагрузкой операторов (не используется в обьектах, предусматривающих
 возможность сохранения)
 """

class Person:
    """Универсальное представление человека: данные + логика"""
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<{} => {}: {}, {}>'.format(self.__class__.__name__, self.name, self.job, self.pay)


class Manager(Person):
    """
    Класс со специализированным методом give_raise,
    наследующий обобщенные методы last_name и __str__
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'maneger')

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(sue, sue.pay, sue.last_name())
    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)
