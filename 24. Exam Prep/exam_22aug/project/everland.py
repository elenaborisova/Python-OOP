from exam_22aug.project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0

        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f'Monthly consumptions: {total_consumption:.2f}$.'

    def pay(self):
        result = ''

        for room in self.rooms:
            if room.budget >= room.expenses:
                total_expenses = room.expenses + room.room_cost
                new_budget = room.budget - total_expenses
                result += f'{room.family_name} paid {total_expenses:.2f}$ ' \
                          f'and have {room.budget:.2f}$ left.\n'
                room.budget = new_budget
            else:
                result += f'{room.family_name} does not have enough budget and must leave the hotel.\n'
                self.rooms.remove(room)

        return result[:-1]

    def status(self):
        result = ''

        total_people_count = sum([room.members_count for room in self.rooms])
        result += f'Total population: {total_people_count}\n'

        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. ' \
                      f'Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'

            for index, child in enumerate(room.children, start=1):
                result += f'--- Child {index} monthly cost: {child.cost:.2f}$\n'

            appliances_cost = sum([app.get_monthly_expense() for app in room.appliances])
            result += f'--- Appliances monthly cost: {appliances_cost:.2f}$\n'

        return result[:-1]
