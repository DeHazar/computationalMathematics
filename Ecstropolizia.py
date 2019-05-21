import math


def factorial(n):
    sum_factorial = 1
    for i in range(1, n + 1):
        sum_factorial *= i
    return sum_factorial


def bernouli(n):
    if n <= 0:
        return 1
    else:
        s = 0
        for k in range(1, n + 1):
            s += bink(n + 1, k + 1) * bernouli(n - k)
        return -1 / (n + 1) * s


# Биномиальный коэффициент Ньютона
def bink(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


# alpha = 1.1
# j = 1
# n = math.pow(2, 1)
# z_exact = 10.5844484649508098
#
# z_n = -1 / (alpha - 1) * math.pow(n, -(alpha - 1)) + 0.5 * math.pow(n, -alpha)
# for i in range(1, j + 1):
#     divisior = 1
#     for k in range(1, i + 1):
#         divisior *= (alpha + 2 * k - 2)
#     divisior = -(divisior * bernouli(2 * i) * math.pow(n, -(alpha + 2 * i - 1))) / factorial(2 * i)
#     z_n += divisior
# z_n = z_exact - z_n
# print(z_n)


# j - степень при n
# z_exact - массив z_n  вычисленных при предыдущем шаге
# возращает массив погрешностей текущий результат минус предыдущий
def extrapolation(j, z_exact):
    alpha = 1.1
    n = []
    zn_zexact = []
    z_n1 = []
    z_n_temp = [10.5844484649508098 - 1 / (alpha - 1) * math.pow(1, -(alpha - 1)) + 0.5 * math.pow(1, -alpha)]
    for degree in range(1, j + 1):
        n.append(math.pow(2, degree))
        z_n = 1 / (alpha - 1) * math.pow(n[-1], -(alpha - 1)) - 0.5 * math.pow(n[-1], -alpha)
        for i in range(1, degree + 1):
            divisior = 1
            for k in range(1, i + 1):
                divisior *= (alpha + 2 * k - 2)
            divisior = (divisior * bernouli(2 * i) * math.pow(n[-1], -(alpha + 2 * i - 1))) / factorial(2 * i)
            z_n += divisior
        z_n = z_exact[degree] - z_n
        z_n1.append(z_n + (z_n - z_n_temp[-1]) / (math.pow(2, alpha) - 1))
        xer = z_n - z_n1[-1]
        xer2 = z_n1[-1] - z_exact[degree]
        z_n_temp.append(z_n)
        zn_zexact.append(z_n - z_exact[degree])
    return z_n_temp


def extrapolation2(j, z_exact):
    alpha = 1.1
    n = []
    zn_zexact = []
    z_n_temp = [z_exact[0] - 1 / (alpha - 1) * math.pow(1, -(alpha - 1)) + 0.5 * math.pow(1, -alpha)]
    for degree in range(1, j + 1):
        n.append(math.pow(2, degree))
        z_n = 1 / (alpha - 1) * math.pow(n[-1], -(alpha - 1)) - 0.5 * math.pow(n[-1], -alpha)
        for i in range(1, degree + 1):
            divisior = 1
            for k in range(1, i + 1):
                divisior *= (alpha + 2 * k - 2)
            divisior = (divisior * bernouli(2 * i) * math.pow(n[-1], -(alpha + 2 * i - 1))) / factorial(2 * i)
            z_n += divisior
        z_n = z_exact[degree] - z_n
        z = z_n + (z_n - z_n_temp[-1]) / (math.pow(2, degree) - 1)
        z_n_temp.append(z_n)
        zn_zexact.append(z_exact[degree] - z)
    return zn_zexact


z_exact = [10.5844484649508098 for i in range(15)]
z_temp = extrapolation(4, z_exact)
print(z_temp)
z_exact2 = extrapolation2(4, z_temp)
print(z_exact2)
