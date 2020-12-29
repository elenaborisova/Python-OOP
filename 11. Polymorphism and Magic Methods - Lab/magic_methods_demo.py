from math import gcd


def simplify(numerator, denominator):
    the_gcd = gcd(numerator, denominator)
    return numerator // the_gcd, denominator // the_gcd


class Fraction:
    def __init__(self, numerator, denominator):
        numerator, denominator = simplify(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        numerator = self.numerator * other.denominator \
                    + other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __ge__(self, other):
        numerator_one = self.numerator * other.denominator
        numerator_two = other.numerator * self.denominator

        return numerator_one == numerator_two \
               or numerator_two > numerator_one


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1)
print(f2)

print(f1 + f2)
print(f1 * f2)

print(f1 >= f2)

print(dir(Fraction))
