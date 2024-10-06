from easy_1 import PoliceCar


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f' машина {self.name} поехала')

    def stop(self):
        print(f' машина {self.name} остановилась')

    def turn(self, direction):
        print(f' машина {self.name} повернула в {direction}')


class TownCar(Car):
    def go(self):
        print('Городская', end='')
        Car.go(self)

    def stop(self):
        print('Городская', end='')
        Car.stop(self)

    def turn(self, direction):
        print('Городская', end='')
        Car.turn(self, direction)


class SportCar(Car):
    def go(self):
        print('Спортивная', end='')
        Car.go(self)

    def stop(self):
        print('Спортивная', end='')
        Car.stop(self)

    def turn(self, direction):
        print('Спортивная', end='')
        Car.turn(self, direction)


class WorkCar(Car):
    def go(self):
        print('Рабочая', end='')
        Car.go(self)

    def stop(self):
        print('Рабочая', end='')
        Car.stop(self)

    def turn(self, direction):
        print('Рабочая', end='')
        Car.turn(self, direction)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

    def go(self):
        print('Полицейская', end='')
        Car.go(self)

    def stop(self):
        print('Полицейская', end='')
        Car.stop(self)

    def turn(self, direction):
        print('Полицейская', end='')
        Car.turn(self, direction)


# Примеры
car_1 = TownCar(60, 'blue', 'Skoda Kodiaq')
car_2 = SportCar(350, 'red', 'La Ferrari F8')
car_3 = WorkCar(70, 'yellow', 'LADA Kalina')
car_4 = PoliceCar(120, 'blue and white', 'Skoda Octavia')

car_1.go()
car_2.stop()
car_3.turn("влево")
car_4.stop()
