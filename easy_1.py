class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Городская машина {self.name} поехала')

    def stop(self):
        print(f'Городская машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Городская машина {self.name} повернула в {direction}')


class SportCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Спортивная машина {self.name} поехала')

    def stop(self):
        print(f'Спортивная машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Спортивная машина {self.name} повернула в {direction}')


class WorkCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Рабочая машина {self.name} поехала')

    def stop(self):
        print(f'Рабочая машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Рабочая машина {self.name} повернула в {direction}')


class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Полицейская машина {self.name} поехала')

    def stop(self):
        print(f'Полицейская машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Полицейская машина {self.name} повернула в {direction}')


# Примеры
car_1 = TownCar(60, 'blue', 'Skoda Kodiaq')
car_2 = SportCar(350, 'red', 'La Ferrari F8')
car_3 = WorkCar(70, 'yellow', 'LADA Kalina')
car_4 = PoliceCar(120, 'blue and white', 'Skoda Octavia')

car_1.go()
car_2.stop()
car_3.turn("влево")
car_4.stop()
