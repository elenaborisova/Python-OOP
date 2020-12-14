class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def can_fill(self, milliliters):
        return milliliters <= self.status()

    def fill(self, milliliters):
        if not self.can_fill(milliliters):
            return

        self.quantity += milliliters

    def status(self):
        free_space = self.size - self.quantity
        return free_space


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
