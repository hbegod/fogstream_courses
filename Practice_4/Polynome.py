# напишите реализацию класса Polynome
class Polynome:

    def __init__(self, list):
        self.coefficients = list

    @staticmethod
    def zip_longest(iter1, iter2, fillchar=None):
        for i in range(max(len(iter1), len(iter2))):
            if i >= len(iter1):
                yield (fillchar, iter2[i])
            elif i >= len(iter2):
                yield (iter1[i], fillchar)
            else:
                yield (iter1[i], iter2[i])
            i += 1

    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [sum(t) for t in Polynome.zip_longest(c1, c2, 0)]
        return Polynome(res)

    def __mul__(self, other):
        if isinstance(other, Polynome):
            _s = self.coefficients
            _v = other.coefficients
            res = [0] * (len(_s) + len(_v) - 1)
            for selfpow, selfco in enumerate(_s):
                for valpow, valco in enumerate(_v):
                    res[selfpow + valpow] += selfco * valco
        else:
            res = [co * other for co in self.coefficients]
        return self.__class__(res)

    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [t1 - t2 for t1, t2 in Polynome.zip_longest(c1, c2, 0)]
        return Polynome(res)

    def calc(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res