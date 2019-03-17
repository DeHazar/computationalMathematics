import numpy as np
import math


def initParams(a: float, b: float, n: int, diferSecond, fun):
    left_matrix = [[0] * n for i in range(n)]
    center_matrix = [0] * n
    right_matrix = [0] * n
    lambda_array = [0] * n
    u_array = [0] * n
    h = (b - a) / n

    x_matrix = [(a + i * h) for i in range(n)]
    left_matrix[0][0] = 1
    left_matrix[0][1] = 0
    right_matrix[0] = 0
    left_matrix[ - 1][-2] = 0
    left_matrix[- 1][-1] = 1
    right_matrix[-1] = 0
    return left_matrix, center_matrix, right_matrix, u_array, h, x_matrix, lambda_array


def splainThird(x, m, h, n, value):
    s = [0] * n
    for i in range(1, n):
        fun = (((x[i] - value) ** 3 - (h ** 2) * (x[i] - value)) * m[i - 1]) / (6 * h) + (
                ((value - x[i - 1]) ** 3 - (h ** 2) * (value - x[i - 1])) * m[i]) / (6 * h) + (
                      (x[i] - value) * s[-2]) / h + ((value - x[i - 1]) * s[-1]) / h
        s[i] = fun
    return s


def calculateSplain(a: float, b: float, n: int,
                    fun, diferFirst, diferSecond):
    left_matrix, center_matrix, right_matrix, u_array, h, x_matrix, lambda_array = initParams(a, b, n,
                                                                                              diferSecond, fun)
    y = []
    for i in range(0, n):
        y.append(fun(x_matrix[i]))
    for i in range(1, n - 1):
        left_matrix[i][i - 1] = h / 6  # Присваеваем коэф с
        left_matrix[i][i] = 2 * h / 3  # коэф а
        if i != n - 1:
            left_matrix[i][i + 1] = h / 6  # коэф b

        right_matrix[i] = (fun(x_matrix[i + 1]) - fun(x_matrix[i])) / h \
                          - (fun(x_matrix[i]) - fun(x_matrix[i - 1])) / h

    lambda_array[0] = -left_matrix[0][1] / left_matrix[0][0]
   # lambda_array[n - 1] = 0
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
                                                 diferFirst=lambda x: math.cos(x), diferSecond=lambda x: -math.sin(x))
    spines = splainThird(x_matrix, center_mas, h, n, 0)
    for s in spines:
        print(s)
