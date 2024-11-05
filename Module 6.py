#Задание 1
names = ["Richard", "Igor", "Jonathan", "Alice", "Mary", "Bonnie"]
for item in names:
    print(f"Hello {item}")
#Задание 2
phrase = "I'm learning cycles."
for i in range(10):
    print(phrase)

#Задание 3
stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for i, station in enumerate(stations):
    if i == len(stations) - 1:
        print(f"Поезд на станции: {station} - Конечная!")
    else:
        print(f"Поезд на станции: {station}")

#Задание 4
shop = ["Laptop", "Smartphone", "Watch", "Tablet", "Headphones"]
for item in shop:
    if "Laptop" in shop:
        print("I'm bying this.")
    else:
        print("I don't need it.")



#Задание 5
tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате", "Подготовить отчёт"]

for index, task in enumerate(tasks, start=1):
    if "(Важная)" in task:
        print(f"{index}: {task}!")
    else:
        print(f"{index}: {task}")
#Задание 6
n = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
total_sum = 0
for i in range(n):
    number = float(input(f"Введите число {i + 1}: "))
    numbers.append(number)
print("Список всех введённых чисел:", numbers)
print("Сумма всех чисел:", total_sum)

#Задание 7
count = 0
while count < 10:
    print(f"Цикл сработал: {count + 1} раз")
    count += 1

#Задание 8
while True:
    command = input("Введите команду (w, a, s, d или stop для выхода): ").strip().lower()
    if command == "w":
        print("Персонаж идёт вперёд.")
    elif command == "a":
        print("Персонаж идёт влево.")
    elif command == "s":
        print("Персонаж идёт назад.")
    elif command == "d":
        print("Персонаж идёт вправо.")
    elif command == "stop":
        print("Программа остановлена.")
        break
    else:
        print("Неизвестная команда! Попробуйте снова.")

#Задание 9
while True:
    number = int(input("Введите число от 1 до 9: "))
    if 1 <= number <= 9:
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Задание 10
otvet = "да"
zagadka = "загадка??"
attempts = 3
print("Загадка:", zagadka)
while attempts > 0:
    answer = input("Ваш ответ: ").strip().lower()
    if answer == otvet:
        print("Поздравляем! Вы угадали!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Неправильно! У вас осталось {attempts} попыток.")
        else:
            print("Все попытки исчерпаны! Загадка была:", otvet)
