class Toy:
    def __init__(self, name, color, type_):
        self.name = name
        self.color = color
        self.type_ = type_

    def _created_toy(self):
        print(f'\nНазвание: {self.name},\nЦвет: {self.color},\nТип: {self.type_},\nИгрушка создана!\n')


class ToyFactory:
    def purchase_materials(self):
        print("Материалы закуплены!")

    def sewn(self):
        print("Игрушка сшита!")

    def painted(self):
        print("Игрушка покрашена!")

    def create_toy(self, name, color, type_):
        self.purchase_materials()
        self.sewn()
        self.painted()
        Toy(name, color, type_)._created_toy()


# Примеры
factory = ToyFactory()
print('первая игрушка')
new_toy_1 = factory.create_toy("Зебра", "Черно-беолого", "Животного")
print('вторая игрушка')
new_toy_2 = factory.create_toy("Медвель", "Коричневый", "Персонаж мультфильма")
