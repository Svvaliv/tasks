class Money:

    def __init__(self, dollars, cents):
        "В конструкторе задаём общее количество количество денег в центах"
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        "Свойство dollars возвращает количество имеющихся у нас долларов"
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        "Свойство сеттер dollars добавляет в копилку указанное количество долларов"
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        "Свойство cents возвращает количество имеющихся у нас центов"
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        "Свойство сеттер cents добавляет в копилку указанное количество центов"
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = self.dollars * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        "Показывает количество имеющихся долларов и центов"
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents)  # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
print(Bill.total_cents)
print(Bill.__dict__.keys())
