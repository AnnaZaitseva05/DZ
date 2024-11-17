# class Vehicle:
#     __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
#
#     def __init__(self, owner, model, color, engine_power):
#         self.owner = str(owner)
#         self.__model = str(model)
#         self.__color = str(color)
#         self.__engine_power = int(engine_power)
#
#     def get_model(self):
#         return f"Модель: {self.__model}"
#
#     def get_horsepower(self):
#         return f"Мощность двигателя: {self.__engine_power}"
#
#     def get_color(self):
#         return f"Цвет: {self.__color}"
#
#     def print_info(self):
#         print(self.get_model())
#         print(self.get_horsepower())
#         print(self.get_color())
#         print(f"Владелец: {self.owner}")
#
#     def set_color(self, new_color):
#         if new_color.lower() in Vehicle.__COLOR_VARIANTS:
#             self.__color = new_color
#         else:
#             print(f'Нельзя сменить цвет на {new_color}')
#
#
#
# class Sedan (Vehicle):
#     __PASSENGERS_LIMIT = 5
#
#
# vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
#
# # Изначальные свойства
#
# vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
#
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
#
# vehicle1.print_info()

import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

# Создаем экземпляр Duckbill с заданной скоростью
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()  # Теперь здесь будет вывод "Be careful, I'm attacking you 0_0"

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

print(Duckbill.mro())
