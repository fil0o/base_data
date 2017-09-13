"""Работа в интерактивном режиме."""
import shelve

fieldnames = ('name', 'age', 'job', 'pay')
max_field = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nkey? => ')  # ключ или пустая строка, вызывает исключение при вводе EOF

    if not key:
        break
    try:
        record = db[key]  # извелю запись по ключу и вывести
    except:
        print('No such key {}!'.format(key))
    else:
        for field in fieldnames:
            print(field.ljust(max_field), '=>', getattr(record, field))
