from restaurant_05.project.food.main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, Salmon.SALMON_GRAMS)
