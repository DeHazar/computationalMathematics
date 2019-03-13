def calculateIntegral(fun, a: float, b: float, degree: int, n: int = 1000):
    """

    :param fun: Функция от которой необходимо вычислить
    :param a: Верхний предел интегрирования
    :param b: Нижний предел
    :param n: Количество разбиений
    :return:
    """
    reachEps = False
    while not reachEps:
        h = (b - a) / n
        x = [(i * h + a) for i in range(n)]
        M1 = (b - a) * max([degree * fun(x[i], degree - 1) for i in range(n)])
        sum = 0
        if 10 ** -5 <= M1 * h / 2:
            n = n + 10000
            continue
        for i in range(n - 1):
            sum += h * fun(x[i], degree)
        return sum


if __name__ == '__main__':
    print(calculateIntegral(lambda x, m: x ** m, a=0, b=2, degree=4, n=2))
