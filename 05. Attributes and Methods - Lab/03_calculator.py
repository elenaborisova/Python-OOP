class Calculator:
    @staticmethod
    def add(*args: int):
        return sum(args)

    @staticmethod
    def multiply(*args: int):
        res = 1
        for num in args:
            res *= num
        return res

    @staticmethod
    def divide(*args):
        res = args[0]
        for num in args[1:]:
            res /= num
        return res

    @staticmethod
    def subtract(*args):
        res = args[0]
        for num in args[1:]:
            res -= num
        return res


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
