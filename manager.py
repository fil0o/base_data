from person_start import Person


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self,name, age, pay, 'manager')

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom)
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)

