class User:
    def __init__(self, username, email, role="user"):
        self.username = username
        self.email = email
        self.role = role

    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}, Role: {self.role}"


class UserAccount(User):
    def __init__(self, username, email, role="user"):
        super().__init__(username, email, role)
        self.__password = None
        self.__failed_attempts = 0
        self.__blocked = False

    def set_password(self, new_password):
        if self.__blocked:
            print("Установка пароля невозможна.")
            return
        self.__password = new_password
        self.__failed_attempts = 0
        print("Пароль успешно установлен.")

    def check_password(self, password):
        if self.__blocked:
            print("Аккаунт заблокирован.")
            return

        if password == self.__password:
            self.__failed_attempts = 0
            print("Вход выполнен успешно!")
        else:
            self.__failed_attempts += 1
            if self.__failed_attempts >= 3:
                self.__blocked = True
                print("Неверный пароль! Попытка 3/3.\nАккаунт заблокирован из-за 3 неудачных попыток.")
            else:
                print(f"Неверный пароль! Попытка {self.__failed_attempts}/3.")

    def reset_password(self, new_password):
        if self.role != "admin":
            print("У вас нет прав для сброса пароля!")
            return
        self.__password = new_password
        self.__failed_attempts = 0
        self.__blocked = False
        print("Пароль сброшен администратором.")

    def increase_failed_attempts(self):
        self.__failed_attempts += 1
        if self.__failed_attempts >= 3:
            self.__blocked = True


# === Пример использования ===
user1 = UserAccount("Ashab", "ashabtamayev@example.com")
admin = UserAccount("AdminUser", "admin@example.com", role="admin")

user1.set_password("securePass123")
user1.check_password("wrongPass")  # 1
user1.check_password("wrongPass")  # 2
user1.check_password("wrongPass")  # 3 (Блокировка)
user1.check_password("securePass123")  # Не сработает

admin.reset_password("newAdminPass")  # Пароль admin'а
user1.reset_password("newUserPass")   # Ошибка
admin.set_password("adminSecurePass")
admin.check_password("adminSecurePass")
