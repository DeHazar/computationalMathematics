import numpy as np


def calculateIntegral(fun, a: float, b: float, degree: int, exact_value: float, n: int = 1000):
    """
    Метод симметричных прямоугольников
    :param fun: Функция от которой необходимо вычислить,  вид а y = m*x^degree
    :param a: Верхний предел интегрирования
    :param b: Нижний предел
    :param n: Количество разбиений
    :param degree: Степень при функции
    :param exact_value: Точное значение интеграла
    :return: возвращает массив нампай с данными
    """
    array_sum = []
    deltaRunge = [0, 0]
    deltaK = [0, 0]
    n_count = [n]
    delta_exact = []
    delta_teorhy = []

    while True:
        h = (b - a) / n
        x = [(i * h + a) for i in range(n)]
        M4 = (b - a) * max([degree * (degree - 1) * (degree - 2)
                            * (degree - 3) * fun(x[i], degree - 4) for i in range(n)])
        sumH = fun(a, degree) + fun(b, degree)

        for i in range(1, n - 1):
            sumH += 2 * fun(x[i], degree)
        for i in range(n - 1):
            sumH += 4 * fun(x[i] + h / 2, degree)

        array_sum.append(sumH * h / 6)
        delta_exact.append(exact_value - sumH * h / 6)
        delta_teorhy.append((M4 / 2880) * h ** 4)

        if len(array_sum) > 2:
            deltaRunge.append((array_sum[-1] - array_sum[-2]) / (2 ** 4 - 1))
            deltaK.append((array_sum[-2] - array_sum[-3]) / (array_sum[-1] - array_sum[-2]))
        else:
            n = 2 * n
            n_count.append(n)
            continue

        if not abs(deltaRunge[-1]) <= 10 ** -6:
            n = 2 * n
            n_count.append(n)
            continue

        return np.array([n_count, deltaK, delta_exact, array_sum, deltaRunge, delta_teorhy])

if __name__ == '__main__':
    data = calculateIntegral(lambda x, m: 3 * x ** m, a=0, b=2, degree=5, n=1, exact_value=32).transpose()

