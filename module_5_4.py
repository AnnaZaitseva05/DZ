class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __radd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors

    def __iadd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors


    def go_to (self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")
        else:
            for num in range(1, new_floor + 1):
                print(num)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)

h1.go_to(5)
h2.go_to(10)

print(h1)
print(h2)
print(len(h1))
print(len(h2))

print(h1 == h2) # __ed__
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
h1 = h1 + 10 # __add__
print(h1)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
