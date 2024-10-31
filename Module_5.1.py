from math import floor

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        floor = 0
        for floor in range(new_floor):
            print(floor + 1)
        new_floor = int (input('Введите номер этажа '))
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')

home = House("ЖК Эльбрус", 30)
home.go_to(30)



