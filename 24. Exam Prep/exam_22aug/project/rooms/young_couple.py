from exam_22aug.project.appliances.fridge import Fridge
from exam_22aug.project.appliances.laptop import Laptop
from exam_22aug.project.appliances.tv import TV
from exam_22aug.project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)
