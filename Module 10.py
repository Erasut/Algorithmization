#Задание 1
import os
import subprocess

class GameLauncher:
    def __init__(self, game_name, executable_path):
        self.game_name = game_name
        self.executable_path = executable_path

    def run(self):
        if os.path.exists(self.executable_path):
            try:
                subprocess.Popen(self.executable_path)
                print(f"Игра {self.game_name} успешно запущена с пути: {self.executable_path}")
            except Exception as e:
                print(f"Ошибка запуска {self.game_name}: {e}")
        else:
            print(f"Ошибка: Игра {self.game_name} не запущена. Путь {self.executable_path} не найден.")

if __name__ == "__main__":
    minecraft = GameLauncher("Minecraft", r"C:\Games\Minecraft\MinecraftLauncher.exe")
    gta5 = GameLauncher("GTA V", r"D:\Rockstar Games\GTA V\GTA5.exe")
    genshin = GameLauncher("Genshin Impact", r"C:\Games\Genshin Impact\GenshinImpact.exe")

    minecraft.run()
    gta5.run()
    genshin.run()

#Задание 2
from abc import ABC, abstractmethod

class File(ABC):
    def __init__(self,filename, size):
        self.filename = filename
        self.size = size
    @abstractmethod
    def open(self):
        pass

    def info(self):
        return f"Имя: {self.filename}, размер: {self.size} кб"

class TextFile(File):
    def __init__(self, filename, size, encoding):
        super().__init__(filename, size)
        self.encoding = encoding
    def open(self):
        print(f"Открытие текстового файла {self.filename} с кодировкой {self.encoding}")

class ImageFile(File):
    def __init__(self, filename, size, resolution):
        super().__init__(filename, size)
        self.resolution = resolution
    def open(self):
        print(f"Открытие изображения {self.filename} с разрешением {self.resolution}")

text_file = TextFile("doc.txt", 177, "utf-8")
image_file = ImageFile("photo.jpg", 2500, "1200x1900")

text_file.open()
image_file.open()

print(text_file.info())
print(image_file.info())

#Задание 3

class Racing_Car:
    def __init__(self, brand, model, color, number):
        self.brand = brand
        self.model = model
        self.color = color
        self.number = number

    def info_car(self):
        print(f"Участник №{self.number}\nАвтомобиль: {self.color} {self.brand} {self.model}")

class Race:
    def __init__(self, name_race):
        self.name_race = name_race
        self.race_cars = []

    def append_participants(self, *cars):
        for car in cars:
            self.race_cars.append(car)


    def __print_participants(self):
        print("Участники гонки:")
        for car in self.race_cars:
            print(f"№{car.number} {car.brand} {car.model}")

    def start_race(self):
        print(f"{self.name_race} скоро старт!")
        self.__print_participants()
        print("Гонка началась.")

car_1 = Racing_Car("BMW", "X4", "черный", 28)
car_1.info_car()

car_2 = Racing_Car("Porsche", "911", "чёрный", 14)
car_2.info_car()

race_1 = Race("Кольцевые автогонки")
race_1.append_participants(car_1, car_2)
race_1.start_race()






