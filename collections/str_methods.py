name = 'Swaroop'  # Это объект строки

if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')

if 'a' in name:
    print('Да, она содержит строку "a"')

if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

date = "02/15/2019"
date.replace(date[5:], '')