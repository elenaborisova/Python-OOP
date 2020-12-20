from hotel_rooms_04.project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_room_by_number(self, room_number: int):
        room = [room for room in self.rooms if room.number == room_number][0]
        return room

    def take_room(self, room_number: int, people: int):
        room = self.get_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result

        self.guests += people

    def free_room(self, room_number: int):
        room = self.get_room_by_number(room_number)
        guests_to_remove = room.guests
        result = room.free_room()
        if result:
            return result

        self.guests -= guests_to_remove

    def print_status(self):
        free_rooms = ", ".join(str(room.number) for room in self.rooms if not room.is_taken)
        taken_rooms = ", ".join(str(room.number) for room in self.rooms if room.is_taken)

        print(f"Hotel {self.name} has {self.guests} total guests")
        if free_rooms:
            print(f"Free rooms: {free_rooms}")
        if taken_rooms:
            print(f"Taken rooms: {taken_rooms}")


hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

hotel.print_status()