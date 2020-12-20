from roman import fromRoman


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if not isinstance(value, float):
            return "value is not a float"

        value = int(value)
        return cls(value)

    @classmethod
    def from_roman(cls, value: str):
        value = fromRoman(value)
        return cls(value)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"

        value = int(value)
        return cls(value)

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"

        result = self.value + integer.value
        return result

    def __str__(self):
        return str(self.value)


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.3"))
print(Integer.from_string(1.5))
print(first_num.add(second_num))
