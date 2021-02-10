from errors import CustomListIndexException, CustomListTypeException, CustomListSumException
from collections import Iterable


class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    @property
    def data(self):
        return self.__data

    def append(self, value) -> list:
        self.__data += [value]
        return self.__data

    def remove(self, index):
        try:
            value_to_remove = self.__data[index]
            del self.__data[index]
            return value_to_remove
        except IndexError as ex:
            raise CustomListIndexException('CustomList cannot find an element on this index!')
        except TypeError as ex:
            raise CustomListTypeException('Index should be of type integer!')

    def get(self, index):
        try:
            return self.__data[index]
        except IndexError as ex:
            raise CustomListIndexException('CustomList cannot find an element on this index!')
        except TypeError as ex:
            raise CustomListTypeException('Index should be of type integer!')

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise CustomListTypeException('This is not an iterable object!')
        self.__data += iterable
        return self.__data

    def insert(self, index, value):
        self.__data = self.__data[:index] + [value] + self.__data[index:]
        return self.__data

    def pop(self):
        value_to_remove = self.__data[-1]
        del self.__data[-1]
        return value_to_remove

    def clear(self):
        self.__data = []

    def index(self, value):
        for index in range(len(self.__data)):
            if self.__data[index] == value:
                return index

        return -1

    def count(self, value):
        counter = 0
        for v in self.__data:
            if v == value:
                counter += 1

        return counter

    def reverse(self):
        return self.__data[::-1]

    def copy(self):
        copy_list = [el for el in self.__data]
        return CustomList(*copy_list)

    def __str__(self):
        return f'{"; ".join([str(el) for el in self.__data])}'

    def size(self):
        return len(self.__data)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        custom_dict = {}

        for i in range(0, len(self.__data), 2):
            key = self.__data[i]
            try:
                value = self.__data[i + 1]
                custom_dict[key] = value
            except IndexError as ex:
                custom_dict[key] = ' '

        return custom_dict

    def move(self, amount):
        self.__data = self.__data[amount:] + self.__data[:amount]
        return self.__data

    def sum(self):
        elements_sum = 0

        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                elements_sum += el
                continue
            try:
                elements_sum += len(el)
            except TypeError as ex:
                raise CustomListSumException('Please provide a len method to custom object!')

        return elements_sum

    def __get_numeric_values(self):
        numeric_elements = []

        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                numeric_elements.append(el)
                continue
            numeric_elements.append(len(el))

        return numeric_elements

    def overbound(self):
        numeric_elements = self.__get_numeric_values()
        return numeric_elements.index(max(numeric_elements))

    def underbound(self):
        numeric_elements = self.__get_numeric_values()
        return numeric_elements.index(min(numeric_elements))
