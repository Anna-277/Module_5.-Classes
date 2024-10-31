class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        for floor in range(new_floor): # Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
            print(floor + 1)
        if new_floor > self.number_of_floors or new_floor < 1: # Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
            print('Такого этажа не существует')

home = House("ЖК Эльбрус", 30)
home.go_to(0)



