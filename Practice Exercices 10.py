#Задание 2
def punct(txt):
    count = sum(1 for char in txt if char in "!?.(),")
    print(count)

punct('(Как дела?)')
----------------------------------------
#Задание 3
def create_cube(x, y):
    for _ in range(y):
        print('*' * x)

create_cube(2, 3)
---------------------------------------
#Задание 1 
def upper(t):
    for char in t:
        if char.isupper():
            print(char, end=' ')
    print()

upper('PriVet')
