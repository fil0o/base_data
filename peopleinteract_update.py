"""Работа в интерактивном режиме."""
import shelve
from person_alternative import Person

fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')

while True:
    key = input('\n key? => ')  # ключ или пустая строка, вызывает исключение при вводе EOF
    if not key:
        break
    if key in db:
        record = db[key]  # изменить существующую записть или создать новую записть для eval: строки в кавычках
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[{}]={}\n\t\tnew? '.format(field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
