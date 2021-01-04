from wild_farm_04.project.animals.animal import Mammal
from wild_farm_04.project.food import Meat, Vegetable, Fruit, Food


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Mouse.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Dog.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, Meat) and not isinstance(food, Vegetable):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Cat.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
