#Задание 1
minutes=int(input())
hours = minutes // 60
ostat = minutes % 60
print(hours)
print(ostat)

#Задание 2
sleep = int(input())
norm = 8
if sleep < norm:
    print("Недосып")
elif sleep > norm:
    print("Пересып")
else:
    print("Это нормально")

#Задание 3
import math
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
s = (a + b + c) / 2#Полупериметр
area = math.sqrt(s * (s - a) * (s - b) * (s - c))#Герон
print(f"Площадь треугольника: {area}")

#Задание 4
figure_type = input("Введите тип фигуры (треугольная, прямоугольная, круглая): ")
if figure_type == 'треугольная':
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))
    s = (a + b + c) / 2
    area = math.sqrt(s  (s - a)  (s - b)  (s - c))
    print(f"Площадь треугольника: {area}")
elif figure_type == 'прямоугольная':
    length = float(input("Введите длину: "))
    width = float(input("Введите ширину: "))
    print(f"Площадь прямоугольника: {area}")
elif figure_type == 'круглая':
    radius = float(input("Введите радиус: "))
    area = 3.14 * radius * 2
    print(f"Площадь круга: {area}")
else:
    print("Неизвестный тип фигуры.")

#Задание 5
n = int(input("Введите количество программистов: "))
if n % 10 == 1 and n % 100 != 11:
    suffix = "программист"
elif 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
    suffix = "программиста"
else:
    suffix = "программистов"
print(f"{n} {suffix}")

#Задание 6
ticket = input("Введите номер билета (6 цифр): ")
if len(ticket) != 6 or not ticket.isdigit():
    print("Номер билета должен содержать 6 цифр.")
else:
    first_half_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second_half_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if first_half_sum == second_half_sum:
        print("Счастливый")
    else:
        print("Несчастливый")
