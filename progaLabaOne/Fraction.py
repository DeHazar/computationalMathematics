def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise TypeError('Не целые числа')

        common = gcd(top, bottom)
        self.num = top // common
        self.den = -bottom // common if bottom < 0 else bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        new_num = self.num * other.den + \
                  self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __truediv__(self, other):
        return self * Fraction(other.den, other.num)

    def __sub__(self, other):
        new_num = self.num * other.den - \
                  self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __ne__(self, other):
        return self.num * other.den != self.den * other.num

    def __radd__(self, other):
        rFraction = Fraction(other, 1)
        sum = rFraction + self
        return sum

    def __iadd__(self, other):
        return self + other

    def __repr__(self):
        return 'Fraction(num = {}, den = {})'.format(self.num, self.den)


def testFraction(first, second):
    print('Сложение: ', end='')
    print(first + second, second + first, sep='  |  ')
    print('Вычитание: ', end='')
    print(first - second, second - first, sep='  |  ')
    print('Деление: ', end='')
    print(first / second, second / first, sep='  |  ')
    print('Умножение: ', end='')
    print(first * second, second * first, sep='  |  ')
    print('Больше или равно   ', end='')
    print(first >= second, second >= first, sep='  |  ')
    print('Меньше или равно  ', end='')
    print(first <= second, second <= first, sep='  |  ')
    print('Не равно или равно  ', end='')
    print(first != second, second == first, sep='  |  ')
    print(repr(first), repr(second), sep='\n')


if __name__ == '__main__':
    fractionOne = Fraction(6, 5)
    fractionTwo = Fraction(1, 5)
    testFraction(fractionOne, fractionTwo)
