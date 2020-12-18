class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.price -= ingredient_price * quantity
        self.ingredients[ingredient] -= quantity

    def pizza_ordered(self):
        self.ordered = True
        ingredients = ', '.join([f"{k}: {v}" for k, v in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {ingredients} and the price will be {self.price}lv."


margarita = PizzaDelivery("Margarita", 11, {"cheese": 2, "tomatoes": 1})
margarita.add_extra("mozzarella", 1, 0.5)
margarita.add_extra("cheese", 1, 1)
margarita.remove_ingredient("cheese", 1, 1)
print(margarita.remove_ingredient("bacon", 1, 2.5))
print(margarita.remove_ingredient("tomatoes", 2, 0.5))
margarita.remove_ingredient("cheese", 2, 1)
print(margarita.pizza_ordered())
print(margarita.add_extra("cheese", 1, 1))