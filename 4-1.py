# ООП
# Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b. Оба поля должны быть типа
# int. Конструктор класса должен принимать параметры a и b и присваивать их полям. Необходимо реализовать следующие
# операции:
# сравнение сложение вычитание умножение деление получение в виде строки
# Операции с дробями должны выполняться как с
# обычными числами, то есть если frac1 и frac2 - объекты класса Fraction, то сложение выполняется так:
# frac1 + frac2
#
# С готовым классом должно быть возможно совершить следующие операции:
# frac1 = Fraction(5, 10)
# frac2 = Fraction(2, 4)
# print(frac1 + frac2)
# >>>Fraction(1, 1)
#
# А сравнение так:
# frac1 == frac2 >>>True frac1 > frac2 >>>False frac1 <= frac2 >>>True
# После создания и выполнения операций дробь
# должна быть сокращена, если это возможно. Например дробь 12/16 должны быть преобразована к 3/4.
#


def gcd(c, z):
    while z != 0:
        c, z = z, c % z
    return c


class Fraction:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.__class__.__name__}{self.a, self.b}"

    def __add__(self, otherfraction):
        newa = self.a * otherfraction.b + self.b * otherfraction.a
        newb = self.b * otherfraction.b
        return Fraction(newa // gcd(newa, newb), newb // gcd(newa, newb))

    def __sub__(self, otherfraction):
        newa = self.a * otherfraction.b - self.b * otherfraction.a
        newb = self.b * otherfraction.b
        return Fraction(newa // gcd(newa, newb), newb // gcd(newa, newb))

    def __mul__(self, otherfraction):
        newa = self.a * otherfraction.a
        newb = self.b * otherfraction.b
        return Fraction(newa // gcd(newa, newb), newb // gcd(newa, newb))

    def __truediv__(self, otherfraction):
        newa = self.a * otherfraction.b
        newb = self.b * otherfraction.a
        return Fraction(newa // gcd(newa, newb), newb // gcd(newa, newb))

    def __eq__(self, other):
        firsta = self.a * other.b
        seconda = other.a * self.b
        return firsta == seconda

    def __lt__(self, other):
        firsta = self.a * other.b
        seconda = other.a * self.b
        return firsta < seconda

    def __le__(self, other):
        firsta = self.a * other.b
        seconda = other.a * self.b
        return firsta <= seconda

    def __ne__(self, other):
        firsta = self.a * other.b
        seconda = other.a * self.b
        return firsta != seconda

    def __gt__(self, other):
        firsta = self.a * other.b
        seconda = other.a * self.b
        return firsta > seconda

    def __ge__(self, other):
        firsta = self.a * other.b
        seconda = other.a * self.b
        return firsta >= seconda

frac1 = Fraction(-3, 3)
frac2 = Fraction(11, 11)
print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
# print(frac1 / frac2)
print(frac1 == frac2)
print(frac1 > frac2)
print(frac1 >= frac2)
print(frac1 != frac2)
print(frac1 <= frac2)
print(frac1 < frac2)
print(frac1)
