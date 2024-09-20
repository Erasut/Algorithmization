#задание 1
first_num = 9
second_num = 7.8
my_str = "start"
print (first_num, second_num, my_str)

first_num = 5.2
print(type(first_num), first_num)

third_num = first_num + second_num
print(type(third_num), third_num)


first_num += 5
second_num += first_num
print(first_num, second_num)

print(int(second_num), first_num)


my_str = "start&stop"
print(my_str)

print(my_str * 5)
#Задание 2
path="C:\\Users\\MainAdmin\\Dekstop\\programs"
print(path)

path="C:\\Users\\MainAdmin\\Dekstop\\programs\\game.exe"
print(path)

path="C:\\Users\\MainAdmin\\Dekstop\\files\\picture.exe"
print(path)

path="C:\\Games\\city simulator" * 2
print(path)
print("Errror path:", path*2)

#Задание 3
num_1 = 7
num_2 = 10
num_3 = 4
summ = num_1 + num_2 + num_3
print("Сумма всех целых чисел:", summ)

num_1 = 7.9
num_2 = 21.3
num_3 = 4.0
summ = num_1 + num_2 + num_3
print("Сумма всех нецелых чисел:", summ)

num_1 = 130
num_2 = 4
num_3 = 2
multiplying = num_1 * num_2 * num_3
print("Умножение всех чисел:", multiplying)

division = num_1 / num_2 / num_3
print("Деление:", division)

num_1 = 2
num_2 = 3
num_3 = 4
degree = num_1 ** num_2 ** num_3
print("Числа в степени:", degree)

num_1 = 2
num_2 = 8
num_3 = 5
math=(43+num_1) + (num_2+67) - (num_3 * 2)
print(math//2)
