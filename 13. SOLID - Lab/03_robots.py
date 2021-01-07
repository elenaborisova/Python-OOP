from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def sensors_count(self):
        pass


class Android(Robot):
    def sensors_count(self):
        return 4


class Chappie(Robot):
    def sensors_count(self):
        return 6


r = Android('type')
print(r.sensors_count())
