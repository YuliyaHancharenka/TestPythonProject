# 'ab' - сокращение от 'a'ddress'b'ook
ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

# Обращаемся ко всем парам ключ-значение нашего словаря, исполь-
# зуя метод items, который возвращает список кортежей, каждый из которых
# содержит пару элементов: ключ и значение
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
ab['Yuliya'] = 'yuliya@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

print("\nАдрес Yuliya'а:", ab['Yuliya'])