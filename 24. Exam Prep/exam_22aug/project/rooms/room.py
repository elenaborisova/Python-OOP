from exam_22aug.project.appliances.appliance import Appliance
from exam_22aug.project.people.child import Child


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children: list = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value <= 0:
            raise ValueError('Expenses cannot be negative')

        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0

        for arg in args:
            for el in arg:
                if isinstance(el, Appliance):
                    total_cost += el.get_monthly_expense()
                elif isinstance(el, Child):
                    total_cost += el.cost

        self.__expenses = total_cost
        return self.__expenses
