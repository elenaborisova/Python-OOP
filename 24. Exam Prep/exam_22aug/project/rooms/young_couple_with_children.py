from exam_22aug.project.appliances.fridge import Fridge
from exam_22aug.project.appliances.laptop import Laptop
from exam_22aug.project.appliances.tv import TV
from exam_22aug.project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2+len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.children, self.appliances)
