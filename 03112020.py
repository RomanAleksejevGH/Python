import math

def perimetr(): #Roman Aleksejev, 03.11.2020, Задача 2.
    print('Вычислить периметр треугольника.')
    while True:
        try:
            a=int(input('Введите сторону "а": '))
            b=int(input('Введите сторону "b": '))
            c=int(input('Введите сторону "c": '))
            print('Периметр треугольника: ',a+b+c)
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            perimetr()
def cenapr(): #Roman Aleksejev, 03.11.2020, Задача 3.
    print('Вычислить цену со скидкой.')
    while True:
        try:
            pr=float(input('Введите цену товара: '))
            dis=float(input('Введите цену скидки: '))
            qa=int(input('Введите количество товара: '))
            va=float((pr-pr*(dis/100.0))*qa)
            print('Общая стоимость: ',round(va,2))
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            cenapr()
def tips(): #Roman Aleksejev, 03.11.2020, Задача 4.
    print('Вычислить на чай с каждого.')
    while True:
        try:
            pr=float(input('Введите цену товара: '))
            tip=float(input('Введите % чаевых: '))
            qa=int(input('Введите количество друзей: '))
            va=float((pr/qa)+(pr*(tip/100.0))/qa)
            print('Каждый заплатит: ',round(va,2))
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            tips()
def dist(): #Roman Aleksejev, 03.11.2020, Задача 5.
    print('Вычислить дистанцию.')
    while True:
        try:
            pr=float(input('Введите скорость: '))
            tip=float(input('Введите время в минутах: '))
            va=float(pr*(tip/60))
            print('Дистанция: ',round(va,2))
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            dist()
def gip(): #Roman Aleksejev, 03.11.2020, Задача 6.
    print('Вычислить гипотенузу треугольника.')
    while True:
        try:
            a=float(input('Введите сторону "а": '))
            b=float(input('Введите сторону "b": '))
            va=math.hypot(a,b)
            print('Каждый заплатит: ',round(va,2))
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            gip()
def con(): #Roman Aleksejev, 03.11.2020, Задача 7.
    print('Конверсия времени.')
    while True:
        try:
            a=int(input('Введите минуты: '))
            b=a//60
            c=round(a%60,2)
            print('Время: ',b,':',c)
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            con()
def conn(): #Roman Aleksejev, 03.11.2020, Задача 8.
    print('Конвертация в двроичную и 16-ю систему из десятичной.')
    while True:
        try:
            a=int(input('Введите число: '))
            b=bin(a)
            c=hex(a)
            print('Число ',a,'в двоичной системе:',b,'в 16-й системе:',c)
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            conn()  
def fuel(): #Roman Aleksejev, 03.11.2020, Задача 9.
    print('Вычислить расход топлива на 100км.')
    while True:
        try:
            a=float(input('Введите количество топлива: '))
            b=float(input('Введите пройденный путь в километрах: '))
            va=a/b*100.0
            print('Расход на 100км: ',round(va,2))
            break
        except ValueError:
            print('Неверное значение! Рестарт...')
            fuel()
def restart():
    while True:
        print('Задача 1 - Периметр треугольника.')
        print('Задача 2 - Вычислить цену со скидкой.')
        print('Задача 3 - Вычислить на чай с каждого.')
        print('Задача 4 - Вычислить дистанцию.')
        print('Задача 5 - Вычислить гипотенузу треугольника.')
        print('Задача 6 - Конверсия времени.')
        print('Задача 7 - Конвертация в двроичную и 16-ю систему из десятичной.')
        print('Задача 8 - Вычислить расход топлива на 100км.')
        flag=input('Выбирите задачу: ')
        if flag=='1':
            perimetr()
            break
        elif flag=='2':
            cenapr()
            break
        elif flag=='3':
            tips()
            break
        elif flag=='4':
            dist()
            break
        elif flag=='5':
            gip()
            break
        elif flag=='6':
            con()
            break
        elif flag=='7':
            conn()
            break
        elif flag=='8':
            fuel()
            break
        else:
            break
restart()   
while True:
        r=input('Еще раз? [y/n]')
        if r=='y':
            restart()
        else:
            break

