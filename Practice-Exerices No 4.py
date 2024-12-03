#Задание 1
number = int(input("Введите целое число: "))
if number < 0:
    print(-number)
elif number == 0:
    print(1)
else:
    print(number)

#Задание 2
user_input = input("Введите произвольную строку: ")
contains_punctuation = '.' in user_input or ',' in user_input
print(contains_punctuation)

#Задание 3
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
if num1 % 3 == 0 and num2 % 3 == 0:
    print(True)
elif num1 % 3 == 0 or num2 % 3 == 0:
    print("Одно число делится на 3")
else:
    print(False)
