from mobile_phone_class import MobilePhone

# Пример использования класса


if __name__ == "__main__":
    phone = MobilePhone("123-456-7890")
    print(phone.turn_on())  # Включаем телефон
    print(phone.call("987-654-3210"))  # Звоним
    print(phone.turn_off())  # Выключаем телефон
    print(phone.call("987-654-3210"))  # Пытаемся позвонить, когда телефон выключен