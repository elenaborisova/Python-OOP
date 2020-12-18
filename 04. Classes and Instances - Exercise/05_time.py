from datetime import datetime, timedelta


class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.time = datetime(100, 1, 1, hours, minutes, seconds)

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.time = datetime(100, 1, 1, hours, minutes, seconds)

    def get_time(self):
        date, time = str(self.time).split()
        return time

    def next_second(self):
        self.time += timedelta(seconds=1)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time2 = Time(10, 59, 59)
print(time2.next_second())

time3 = Time(23, 59, 59)
print(time3.next_second())