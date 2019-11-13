def zip_longest(iter1, iter2, fillvalue=None):
    for i in range(max(len(iter1), len(iter2))):
        if i >= len(iter1):
            yield (fillvalue, iter2[i])
        elif i >= len(iter2):
            yield (iter1[i], fillvalue)
        else:
            yield (iter1[i], iter2[i])
        i += 1


class Polynome:

    def __init__(self, *coefficients):
        if len(coefficients) == 1:
            self.coefficients = coefficients[0]
        else:
            self.coefficients = [i+0 for i in coefficients]

    def __repr__(self):
        return f"{__class__.__name__}{tuple(self.coefficients)}"

    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return self.__class__(res)

    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [t1 - t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return self.__class__(res)

    def calc(self, val):
        c = self.coefficients
        res = 0
        for i in range(len(c)):
            res = res + c[i] * val ** i
        return res

    def __mul__(self, val):
        c1 = self.coefficients
        c2 = val.coefficients
        res = [0] * (len(c1) + len(c2) - 1)
        for selfpow, selfco in enumerate(c1):
            for valpow, valco in enumerate(c2):
                res[selfpow + valpow] += selfco * valco
        return self.__class__(res)


coef1 = [-5, 15, -16, 11]
coef2 = [1, -5, 2, 23]
poly1 = Polynome(coef1)
poly2 = Polynome(coef2)
poly3 = Polynome(2, 3)
poly4 = Polynome(4, 5)
print(poly1 + poly2)
print(poly3 * poly4)
# >>>Polynome(-4, 10, -14, 34)
print(poly1 - poly2)
# >>>Polynome(-6, 20, -18, -12)
print(poly1.calc(5))
# >>>1045
