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
