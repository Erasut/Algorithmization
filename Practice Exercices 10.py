#Задание 2
def punct(txt):
    count = sum(1 for str in txt if str in "!?.(),")
    print(count)

punct('(Как дела?)')

#Задание 3
def create_cube(x, y):
    for _ in range(y):
        print('*' * x)

create_cube(2, 3)

#Задание 1 
def upper(t):
    for str in t:
        if str.isupper():
            print(str, end=' ')
    print()

upper('PriVet')

