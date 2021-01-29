class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        if not value:
            raise Exception('Make cannot be null or empty!')
        self.__make = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value:
            raise Exception('Model cannot be null or empty!')
        self.__model = value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value <= 0:
            raise Exception('Fuel consumption cannot be zero or negative!')
        self.__fuel_consumption = value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, value):
        if value <= 0:
            raise Exception('Fuel capacity cannot be zero or negative!')
        self.__fuel_capacity = value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        if value < 0:
            raise Exception('Fuel amount cannot be negative!')
        self.__fuel_amount = value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception('Fuel amount cannot be zero or negative!')
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed
