#Задание 1
minutes=int(input())
hours = minutes // 60
ostat = minutes % 60
print(hours)
print(ostat)

#Задание 2
sleep = int(input())
norm = 8
if sleep < norm:
    print("Недосып")
elif sleep > norm:
    print("Пересып")
else:
    print("Это нормально")

#Задание 3
