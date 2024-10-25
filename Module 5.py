#Задание 1
age=int(input())
if age < 18:
    print("Вы несовершеннолетний")
elif age > 18 and age <= 65:
    print("Вы трудоспособный человек")
else:
    print("Вы пенсионер")

#Задание 2
summa = int(input())
if summa < 1000:
    print("Скидки нет")
elif summa >= 1000 and summa <= 5000:
    print("Скидка 5%", summa * 0,05)
else:
    print(summa * 0.1)
#Задание 3
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = input("Введите операцию")
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("Введена неверная операция")
-------------------------------------------
#Задание 4
x = int(input())
if  x % 2 == 0 and x % 2 == 2 or x % 2 == 6:
    print("True")
else:
    print("False")
--------------------------------------------
#Задание 5
a = int(input())
x = 18452
if a != x:
    print("Доступ запрещён")
else:
    print("Доступ разрешён")
#Задание 6
coordinate = coordinate.upper()
if coordinate in squares:
    color = squares[coordinate]
    if color == 'green':
        return "В данном квадрате обитает зеленый попугай."
    elif color == 'blue':
        return "В данном квадрате обитает синий попугай."
    elif color == 'gray':
        return "В данном квадрате никто не сидит."
else:
    return "Некорректные координаты."
#Задание 7
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
if k != 0 and n % k == 0:
    print(f"{n} кратно {k}")
else:
    print(f"{n} не кратно {k} или k равно 0")

#Задание 8
lvl=input()
health=int(input())
if lvl >= 5:
elif health > 50 and health<= 100:
    print("Вы готовы к миссии!")
elif health >= 20 and health <= 50:
    print("Ваше здоровье низкое, будьте осторожны.")
elif health <20:
    print("Ваше здоровье слишком низкое для выполнения миссии.")
else:
    print("Некорректные данные.")



