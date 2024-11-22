#Задание 1
def create_car(brand: str, color: str, max_speed: int) -> str:
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
