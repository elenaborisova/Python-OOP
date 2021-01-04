from wild_farm_04.project.animals.animal import Bird
from wild_farm_04.project.food import Meat, Vegetable, Fruit, Food


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Owl.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += Hen.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


owl = Owl("Pip", 10, 10)
print(owl)

meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)

veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)

print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
