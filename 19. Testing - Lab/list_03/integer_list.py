class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    @property
    def data(self):
        return self.__data

    @staticmethod
    def validate_type(element):
        if not type(element) == int:
            raise ValueError('Element is not Integer')

    def validate_index(self, index):
        if index >= len(self.data):
            raise IndexError('Index is out of range')

    def add(self, element):
        self.validate_type(element)

        self.data.append(element)
        return self.data

    def remove_index(self, index):
        self.validate_index(index)

        element = self.data[index]
        del self.data[index]
        return element

    def get(self, index):
        self.validate_index(index)

        return self.data[index]

    def insert(self, index, el):
        self.validate_index(index)
        self.validate_type(el)

        self.data.insert(index, el)

    def get_biggest(self):
        return max(self.data)

    def get_index(self, el):
        return self.data.index(el)
