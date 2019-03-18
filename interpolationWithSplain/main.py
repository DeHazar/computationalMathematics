import numpy as np
import math


def initParams(a: float, b: float, n: int, diferSecond):
    """
    Иницилизирует начальные данные
    :param a: левая граница
    :param b: правая граница
    :param n: количество разбиений
    :param diferSecond: лямбда второй производной
    :return: Возврашает проинецилизорованые данные
    """
    left_matrix = [[0] * n for i in range(n)]
    center_matrix = [0] * n
    right_matrix = [0] * n
    lambda_array = [0] * n
    u_array = [0] * n
    h = (b - a) / n

    x_matrix = [(a + i * h) for i in range(n)]
    left_matrix[0][0] = 1
    left_matrix[0][1] = 0
    left_matrix[- 1][-2] = 0
    left_matrix[- 1][-1] = 1
    right_matrix[0] = diferSecond(a)
    right_matrix[-1] = diferSecond(b)

    return left_matrix, center_matrix, right_matrix, u_array, h, x_matrix, lambda_array


def splainThird(x, m, h, n, value, fun):
    """

    :param x: матрица левая
    :param m: матрица решений
    :param h: шаг
    :param n: количество разбиений
    :param value:
    :param fun:
    :return:
    """
    index = -1
    for i in range(n - 1):
        if x[i] <= value <= x[i + 1]:
            index = i + 1
            break

    splain_value = (((x[index] - value) ** 3 - (h ** 2) * (x[index] - value)) * m[index - 1]) / (6 * h) + (
            ((value - x[index - 1]) ** 3 - (h ** 2) * (value - x[index - 1])) * m[index]) / (6 * h) + (
                           (x[index] - value) * fun(x[index - 1])) / h + ((value - x[index - 1]) * fun(x[index])) / h
    return splain_value


def calculateSplain(a: float, b: float, n: int,
                    fun, diferSecond):
    """
    Расчет массивов методом прогонки
    :param a: левая граница
    :param b: правая граница
    :param n: количество разбиений
    :param fun: лямбда функция искомой функции
    :param diferSecond: лямбда второй производной
    :return: Матрицу коэффициентов, матрицу решений, количество разбиений, шаг
    """
    left_matrix, center_matrix, right_matrix, u_array, h, x_matrix, lambda_array = initParams(a, b, n,
                                                                                              diferSecond)
    for i in range(1, n - 1):
        left_matrix[i][i - 1] = h / 6  # Присваеваем коэф с
        left_matrix[i][i] = 2 * h / 3  # коэф а
        if i != n - 1:
            left_matrix[i][i + 1] = h / 6  # коэф b

        right_matrix[i] = (fun(x_matrix[i + 1]) - fun(x_matrix[i])) / h - (fun(x_matrix[i]) - fun(x_matrix[i - 1])) / h

    # massiv_left = np.array(left_matrix)
    # massiv_right = np.array(right_matrix)
    # answer = np.linalg.solve(massiv_left, massiv_right)

    lambda_array[0] = -left_matrix[0][1] / left_matrix[0][0]
    u_array[0] = right_matrix[0] / left_matrix[0][0]

    for i in range(1, n):
        if not i == n - 1:
            lambda_array[i] = -left_matrix[i][i + 1] / (
                    (left_matrix[i][i]) + left_matrix[i][i - 1] * lambda_array[i - 1])

        u_array[i] = (right_matrix[i] - left_matrix[i][i - 1] * u_array[i - 1]) / (
                left_matrix[i][i] + left_matrix[i][i - 1] * lambda_array[i - 1])

    center_matrix[n - 1] = u_array[n - 1]
    for i in range(n - 2, 0, -1):
        center_matrix[i] = lambda_array[i] * center_matrix[i + 1] + u_array[i]

    return x_matrix, center_matrix, n, h


if __name__ == '__main__':
    x_matrix, center_mas, n, h = calculateSplain(a=0.0, b=math.pi, n=100, fun=lambda x: math.sin(x),
                                                 diferSecond=lambda x: -math.sin(x))
    spine = splainThird(x_matrix, center_mas, h, n, math.pi / 2, fun=lambda x: math.sin(x))
    print(spine)
