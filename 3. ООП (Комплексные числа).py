# ООП
# Создать класс Complex, который должен иметь два поля: действительная часть real и мнимая часть imag. Оба поля
# должны быть типа int. Конструктор класса должен принимать параметры real и imag и присваивать их соответствующим
# полям. Реализовать сложение, вычитание, умножение и деление комлексных чисел. Операции с комлексными числами должны
# выполняться как с обычными, то есть если compl1 и compl2 - объекты класса Complex, то сложение выполняется так:
#
# compl1 + compl2
# Также следует реализовать метод для строкового представления объектов типа Complex для вывода на
# печать или непосредственного получения строкового значения в коде вызовом встроенной функции str(c). С готовым
# классом должно быть возможно совершить следующие операции:
#


class Complex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __div__(self, other):
        sreal, simag = self.real, self.imag
        oreal, omag = other.real, other.imag
        r = float(oreal ** 2 + omag ** 2)
        return Complex((sreal * oreal + simag * omag) / r,
                       (simag * oreal - sreal * omag) / r)

    # def __str__(self):
    #     return f"({self.real:.2f}{self.imag:+.2f}j)"
    def __str__(self):
        return f"({self.real:.2f}{(self.imag):+.2f}j)"
        # return f"({self.real:.2f}{'%+.2f' % self.imag}j)"

a1 = -66.7231615894444
a2 = 79.2111027243719
b1 = -39.310586476702625
b2 = 70.69525050590892
compl1 = Complex(a1, b1)
compl2 = Complex(a2, b2)
print(compl1, compl2, compl1 + compl2)
# >>> (-66.72-39.31j) (79.21+70.70j) (12.49+31.38j)
print(compl1 * compl2)
# >>> (-2506.14-7830.85j)
