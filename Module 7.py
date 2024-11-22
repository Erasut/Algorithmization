#Задание 1
def create_car(brand: str, color: str, max_speed: int) -> str:
    return f"Марка: {brand} Цвет: {color} Максимальная скорость: {max_speed} км/ч"
car_info = create_car("Mercedes", "Черный", 350)
print(car_info)
