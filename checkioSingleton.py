class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Capital(metaclass=Singleton):
    def __init__(self, city_name):
        self.city_name = city_name

    def name(self):
        return self.city_name



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")
    print(ukraine_capital_2.name())  #== "Kyiv"
    print(ukraine_capital_3.name())  # == "Kyiv"
