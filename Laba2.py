def calculateIntegral(fun, a: float, b: float, degree: int, n: int = 1000):
    """
    Метод симметричных прямоугольников
    :param fun: Функция от которой необходимо вычислить,  вид а y = m*x^degree
    :param a: Верхний предел интегрирования
    :param b: Нижний предел
    :param n: Количество разбиений
    :param degree: Степень при функции
    :return:
    """
    reachEps = False
    while not reachEps:
        h = (b - a) / n
        x = [(i * h + a) for i in range(n)]
        M2 = (b - a) * max([degree*(degree-1) * fun(x[i], degree - 2) for i in range(n)])
        sumH = 0
        sumHalfH = 0

        for i in range(n - 1):
            sumH += h * fun(x[i]+h/2, degree)
            sumHalfH += h * fun(x[i]+h/2, degree)/2

        deltaRunge = (sumHalfH - sumH)/(2 ** 2 - 1)

        if not deltaRunge <= 10 ** -6:
            n = 2*n
            continue
        # if 10 ** -6 <= M2 * h**2 / 24:
        #     n = 2*n
        #     continue
        return sumH


if __name__ == '__main__':
    print(calculateIntegral(lambda x, m: 6*x ** m, a=0, b=1, degree=5, n=2))
