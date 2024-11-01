#Задание 1
names = ["Richard", "Igor", "Jonathan", "Alice", "Mary", "Bonnie"]
for x in names:
    print(f"Hello {x}!")

#Задание 2
phrase = "I'm learning cycles."
for x in range(10):
    print(phrase)
    
#Задание 3
stations = ["Малиновка", "Рябиновка", "Суслово", "Дрожжино", "Звягино"]
for i, x in enumerate(stations):
    if i == len(stations) - 1:
        print(f"Поезд на станции: {x} (Конечная!)")
    else:
        print(f"Поезд на станции: {x}")

#Задание 4
shop = ["Laptop", "Smartphone", "Watch", "Tablet", "Headphones"]
for x in shop:
    if x == "Laptop":
        print("I'm buying this.")
        break
    else:
        print("I don't need it.")
        break
#Задание 5
tasks = ["Сдать проект (Важная)", "Сходить в магазин", "Позвонить врачу (Важная)", "Убраться в комнате", "Подготовить отчёт"]
for i, x in enumerate(tasks, start=1):
    if "Важная" in x:
        print(f"{i}!: {x} ")
    else:
        print(f"{i} : {x}")

#Задание 6
num_c = int(input("Сколько чисел вы хотите ввести? "))
nums = []
sum = 0
for x in range(num_c):
    number = float(input("Введите число: "))
    nums.append(number)
    sum += number
print("Список всех введённых чисел:", nums)
print("Сумма всех чисел:", sum)

#Задание 7
counter = 1
while counter <= 10:
    print(f" Цикл сработал {counter}") 
    counter += 1

#Задание 8
while True:
    com = input("Введите команду (w - вперед, a - влево, s - назад, d - вправо, stop - выйти): ")
    if com == "w":
        print("Персонаж идет вперед.")
    elif com == "a":
        print("Персонаж идет влево.")
    elif com == "s":
        print("Персонаж идет назад.")
    elif com == "d":
        print("Персонаж идет вправо.")
    elif com == "stop":
        print("Программа остановлена.")
        break
    else:
        print("Неизвестная команда! Попробуйте снова.")

#Задание 9
while True:
    try:
        num = int(input("Введите число от 1 до 9: "))
        if 1 <= num <= 9:
            break
        else:
            print("Число вне диапазона. Пожалуйста, попробуйте снова.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
print(f"Таблица умножения для числа {num}:")
for x in range(1, 11):
    res = num * x
    print(f"{num} x {x} = {res}")

#Задание 10
secret_answer = "слон"
attempts = 3
print("Загадка: Я большой и серый, у меня длинный хобот. Кто я?")
while attempts > 0:
    answer = input(
        "Ваш ответ: ").strip().lower()
    if answer == secret_answer:
        print("Поздравляем! Вы угадали!")
        break
    else:
        attempts -= 1
        print(f"Неправильный ответ. У вас осталось {attempts} попыток.")
if attempts == 0:
    print("Все попытки исчерпаны. Загадка осталась неразгаданной.")
