class Hotel:
    def __init__(self, hotel ):
        self.hotel = hotel
        self.rooms = {100: True, 101: True, 102: True, 103: True,
                 200: True, 201: True, 202: True, 203: True}
    def print_rooms(self):
        print(self.hotel)
        for room, available in self.rooms.items():
            status = "свободно"if available else "занят"
            print(f"Номер № {room} {status}")
    def book_room_number(self, room_number):
        if room_number not in self.rooms:
            print("Ошибка! такого номера нет.")
        elif not self.rooms[room_number]:
            print(f"Номер {room_number} уже забронирован.")
        else:
            self.rooms[room_number] = False
            print(f"Номер {room_number} успешно забронирован.")
    def finish_number_by_number(self, room_number):
        if room_number not in self.rooms:
            print("Ошибка! Такого номера нет.")
        elif self.rooms[room_number]:
            print(f"Номер {room_number} не забронирован.")
        else:
            self.rooms[room_number] = True
            print(f"Бронь номера {room_number} успешно снята.")

hotel = Hotel("ОТель: У Егора")
hotel.print_rooms() 
