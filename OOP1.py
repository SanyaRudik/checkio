# Создаем класс Car
class Car:
    # создаем атрибуты класса

    # создаем методы класса
    car_count = 0

    # создание методов класса
    def __init__(self):
        print("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999
    # создание методов класса
    def __str__(self):
        return "Car class Object"

    @staticmethod
    def get_class_details():
        print("Это класс Car")

    # создаем методы класса
    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    def stop(self):
        print("Отключаем двигатель")


class Square:

    @staticmethod
    def get_squares(a, b):
        return a * a, b * b


# print(Square.get_squares(3, 5))
# car_a = Car()
# car_a.start("Corrola", "Toyota", 2015)
# print(car_a.name)
# print(car_a.car_count)
# car_b = Car()
# car_b.start("City", "Honda", 2013)
# print(car_b.name)
# print(car_b.car_count)
# Car.get_class_details()
# print(Square.get_squares(3, 5))
# print(car_a)
car_a = Car()
car_b = Car()
car_c = Car()
