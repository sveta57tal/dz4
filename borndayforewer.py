"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def pyshkin(who='А.С.Пушкина', y='1799'):
    year = input('Ввведите год рождения {}:'.format(who))
    while year != format(y):
        print("Не верно")
        year = input('Ввведите год рождения {}:'.format(who))

    day = input('Ввведите день рождения {}:'.format(who))
    while day != '6':
        print("Не верно")
        day = input('В какой день июня родился {}:'.format(who))
    print('Верно')

print(pyshkin())