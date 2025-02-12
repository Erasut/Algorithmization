#Задание 1
class Pers():
    def __init__(self, name, klass, hp, damage):
        self.name = name
        self.klass = klass
        self.hp = hp
        self.damage = damage

    def print_info(self):
        print(f"Имя: {self.name}")
        print(f"Класс: {self.klass}")
        print(f"Жизни: {self.hp}")
        print(f"Урон: {self.damage}")
        print("-" * 30)

    def go(self):
        print(f"{self.name} отправился гулять!")
        print("-"*30)

    def nazad(self):
        print(f"{self.name} пришёл домой")

    def start_training(self):
        print(f"{self.name} начал качаться")
        self.hp +=10
        self.damage += 5
        print(f"После качалки он стал круче")
        print(f"Новые жизни: {self.hp}, Новый урон: {self.damage}")
        print("-" * 30)

    def start_draka(self):
        print(f"{self.name} готовится к забиву")
        self.print_info()

hero = Pers(name = "Арутр", klass = "Ковбой", hp=120, damage=30)
hero.print_info()
hero.go()
hero.start_training()
hero.start_draka()
hero.nazad()
------------------------------------------------------------------------

#Задание 2
class Room:
    def __init__(self, name, area=None):
        self.name = name
        self.items = []
        self.locked = False
        self.theme = None
        self.area = area

    def add_item(self, *items):
        if not self.locked:
            self.items.extend(items)
        else:
            print(f"Комната {self.name} закрыта. Невозможно добавить предметы.")

    def del_item(self, item):
        if not self.locked:
            if item in self.items:
                self.items.remove(item)
            else:
                print(f"Предмет {item} не найден в комнате {self.name}.")
        else:
            print(f"Комната {self.name} закрыта. Невозможно удалить предметы.")

    def print_items(self):
        print(f"Все предметы в комнате {self.name}: {', '.join(self.items)}")

    def find_item(self, item):
        return item in self.items

    def count_items(self):
        return len(self.items)

    def clear_items(self):
        if not self.locked:
            self.items.clear()
        else:
            print(f"Комната {self.name} закрыта. Невозможно очистить предметы.")

    def replace_item(self, old_item, new_item):
        if not self.locked:
            if old_item in self.items:
                index = self.items.index(old_item)
                self.items[index] = new_item
            else:
                print(f"Предмет {old_item} не найден в комнате {self.name}.")
        else:
            print(f"Комната {self.name} закрыта. Невозможно заменить предметы.")

    def move_item_to(self, item, another_room):
        if not self.locked:
            if item in self.items:
                self.items.remove(item)
                another_room.add_item(item)
            else:
                print(f"Предмет {item} не найден в комнате {self.name}.")
        else:
            print(f"Комната {self.name} закрыта. Невозможно переместить предметы.")

    def rename_room(self, new_name):
        self.name = new_name

    def describe_room(self):
        description = f"Комната {self.name}"
        if self.area:
            description += f", площадь: {self.area} м²"
        if self.theme:
            description += f", тематика: {self.theme}"
        description += f". Предметы: {', '.join(self.items)}"
        print(description)

    def merge_rooms(self, another_room):
        if not self.locked and not another_room.locked:
            self.items.extend(another_room.items)
            another_room.clear_items()
        else:
            print("Одна из комнат закрыта. Невозможно объединить.")

    def is_empty(self):
        return len(self.items) == 0

    def get_room_size(self):
        return self.area

    def lock_room(self):
        self.locked = True

    def unlock_room(self):
        self.locked = False

    def is_locked(self):
        return self.locked

    def filter_items_by_keyword(self, keyword):
        return [item for item in self.items if keyword.lower() in item.lower()]

    def get_items_starting_with(self, letter):
        return [item for item in self.items if item.lower().startswith(letter.lower())]

    def count_specific_item(self, item):
        return self.items.count(item)

    def list_items_by_type(self, item_type):

        return [item for item in self.items if item_type.lower() in item.lower()]

    def add_decor(self, item):
        self.items.append(item)

    def set_theme(self, theme):
        self.theme = theme

    def show_theme(self):
        return self.theme


room1 = Room ("Кухня", 15)
room2 = Room ("Гостиная", 20)

room1.add_item("Холодильник", "Стул", "Стол")
room2.add_item("Диван", "Телевизор", "Ковер")

room1.print_items()
room2.print_items()

room1.move_item_to("Стул", room2)

room1.print_items()
room2.print_items()

room1.rename_room("Современная кухня")
room1.describe_room()

room1.merge_rooms(room2)
room1.describe_room()
room2.describe_room()

print(f"Комната {room2.name} пустая: {room2.is_empty()}")

print(f"Предметы в комнате {room1.name}, содержащие 'Ст': {room1.filter_items_by_keyword('Ст')}")

room1.set_theme("Современный стиль")
print(f"Тематика комнаты {room1.name}: {room1.show_theme()}")

room1.lock_room()
room1.add_item("Микроволновка")
---------------------------------------------------------------------------------------------------
#Задание 3
class Car:
    def __init__(self, brand, model, km, year):
        self.brand = brand
        self.model = model
        self.km = km
        self.year = year

    def show_info(self):
        print(f"Автомобиль: {self.brand} {self.model}, Год выпуска: {self.year}, Пробег: {self.km} км")

    def update_mileage(self, new_km):
        if new_km >= self.km:
            self.km = new_km
            print(f"Пробег обновлен до {self.km} км")
        else:
            print("Ошибка: Новый пробег не может быть меньше текущего.")

    def is_new(self):
        if self.km < 10000:
            print("Это новый автомобиль.")
        else:
            print("Это не новый автомобиль.")

    def update_km(self, param):
        pass


car1 = Car("Toyota", "Corolla", 5000, 2020)
car2 = Car("Ford", "Mustang", 15000, 2018)

car1.show_info()
car1.update_km(6000)
car1.is_new()

car2.show_info()
car2.update_km(14000)
car2.is_new()

class Phone:
    def __init__(self, brand, model, battery_capacity, charge):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.charge = charge

    def charge_phone(self, amount):
        if amount > 0:
            self.charge = min(self.charge + amount, self.battery_capacity)
            print(f"Телефон заряжен до {self.charge} мАч")
        else:
            print("Ошибка: Количество заряда должно быть положительным.")

    def spend_charge(self, amount):
        if amount > 0:
            self.charge = max(self.charge - amount, 0)
            print(f"Заряд телефона уменьшен до {self.charge} мАч")
        else:
            print("Ошибка: Количество потраченного заряда должно быть положительным.")

    def is_discharged(self):
        if self.charge == 0:
            print("Телефон разряжен.")
        else:
            print(f"Телефон заряжен. Текущий заряд: {self.charge} мАч")


phone1 = Phone("Samsung", "Galaxy S21", 4000, 2000)
phone2 = Phone("Apple", "iPhone 12", 3000, 3000)

phone1.charge_phone(1000)
phone1.spend_charge(500)
phone1.is_discharged()

phone2.charge_phone(-100)
phone2.spend_charge(3500)
phone2.is_discharged()
