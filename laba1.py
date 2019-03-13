import math


def findMinGradFunction(a: float, b: float, c: float, d: float, eps: float = 0.00001):
    x = [0]
    y = [0]
    dx = [a + 2 * c * math.exp(c * x[-1] ** 2 + d * y[-1] ** 2)]
    dy = [b + 2 * d * math.exp(c * x[-1] ** 2 + d * y[-1] ** 2)]
    alpha = [1]
    result = {}

    def popArrays():
        x.pop()
        y.pop()
        dx.pop()
        dy.pop()

    def f(x, y):
        z = a * x + b * y + math.exp(c * x ** 2 + d * y ** 2)
        return z

    while True:
        x.append(x[-1] - alpha[-1] * dx[-1])
        y.append(y[-1] - alpha[-1] * dy[-1])

        dx.append(a + 2 * c * x[-1] * math.exp(c * x[-1] ** 2 + d * y[-1] ** 2))
        dy.append(b + 2 * d * y[-1] * math.exp(c * x[-1] ** 2 + d * y[-1] ** 2))

        if abs(dx[-1]) < eps / 2 and abs(dy[-1]) < eps / 2:
            result['x'] = x
            result['y'] = y
            result['dx'] = dx
            result['dy'] = dy
            result['alpha'] = alpha
            return result

        if f(x[-1], y[-1]) > f(x[-2], y[-2]):
            alpha.append(alpha[-1] / 2)
            popArrays()
        elif f(x[-1], y[-1]) < f(x[-2], y[-2]):
            alpha.pop()


result = findMinGradFunction(a=11, b=-0.4, c=1, d=0.21)

for x in result:
    print(x, end='           |')

print('')
for i in range(len(result['x'])):
    print(result['x'][i],result['y'][i],result['dx'][i],result['dy'][i], sep='   |')

print('alpha = ', result['alpha'])