class MobilePhone:
    def __init__(self, number):
        self.number = number
        self.switch = False  # Изначально телефон выключен

    def turn_on(self):
        self.switch = True
        return f'mobile phone {self.number} is enabled'

    def turn_off(self):
        self.switch = False
        return f'mobile phone {self.number} is turned off'

    def call(self, cally):
        if self.switch:
            return f'calling {cally}'
        else:
            return f'cannot call {cally}, mobile phone {self.number} is turned off'