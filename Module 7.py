#Задание 1
def create_car(brand: str, color: str, max_speed: int):
    return f"Марка: {brand} Цвет: {color} Максимальная скорость: {max_speed} км/ч"
car_info = create_car("Mercedes", "Черный", 350)
print(car_info)

#Задание 2
def switch_check(switch):
    if switch is True:
        print("True работает")
    elif switch is False:
        print("False не работает")
    else:
        print(f"{switch} сломан.")
switch_1 = True
switch_2 = False
switch_3 = None
switch_check(switch_1)
switch_check(switch_2)
switch_check(switch_3)

#Задание 3.1
def triangle_type(side1: float, side2: float, side3: float):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        if side1 == side2 == side3:
            print("Равносторонний треугольник")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("Равнобедренный треугольник")
        else: 
            print("Разносторонний треугольник")
    else: 
        print("Некорректные стороны. Невозможно построить треугольник.")
triangle_type(3, 3, 3)
triangle_type(5, 5, 8)
triangle_type(3, 4, 5)
triangle_type(1, 2, 3)

#Задание 3.2
import math
def triangle(a, b, c):
    print("Длина сторон треугольника:", a, b, c, "\nИнформация:")
    if a + b <= c or a + c <= b or c + b <= a:
        print("Некорректные стороны. Невозможно построить треугольник.")
    elif a != b and a != c and b != c:
        print("Разносторонний треугольник")
    elif a == b or a == c or b == c:
        print("Равнобедренный треугольник")
    elif a == b == c:
        print("Равносторонний треугольник")
    p = (a + b + c)
    s = p / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Площадь: {int(s)}\nПериметр: {round(area, 2)}")

#Задание 4 
def number_change(input_number, output_number):
    steps = 0 
    while input_number != output_number:
        if input_number < output_number:
            input_number += 1  
        elif input_number > output_number:
            input_number -= 1 
        steps += 1 
    return steps, input_number, output_number
result = number_change(5, 10)
print(result) 
