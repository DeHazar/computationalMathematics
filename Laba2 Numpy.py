
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[68]:



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
    n_count =[n]
    delta_exact =[]
    delta_teorhy =[]

    while True:
        h = (b - a) / n
        x = [(i * h + a) for i in range(n+1)]
        M4 = (b - a) * 720
        sumH = fun(a, degree) + fun(b, degree)
    
        for i in range(1, n ):
            sumH += 2*fun(x[i], degree)
        for i in range(n ):
            sumH += 4 * fun(x[i] + h / 2, degree)
        
        array_sum.append(sumH*h/6)
        delta_exact.append(exact_value - sumH*h/6)
        delta_teorhy.append((M4/2880)*h**4)
        
        if len(array_sum) > 2:
            deltaRunge.append((array_sum[-1] - array_sum[-2]) / (2 ** 4 - 1))
            deltaK.append((array_sum[-2] - array_sum[-3])/(array_sum[-1] - array_sum[-2]))
        else:
            n = 2 * n
            n_count.append(n)
            continue
        if (not abs(deltaRunge[-1]) <= 10 ** -16) or n >= 70000:
            n = 2 * n
            n_count.append(n)
            continue
        
        return np.array([n_count, deltaK,delta_exact, array_sum, deltaRunge, delta_teorhy])
    


# In[69]:


data = calculateIntegral(lambda x, m: 6*x ** m, a=0, b=1, degree=5, n=1 , exact_value=1).transpose()


# In[ ]:


df = pd.DataFrame(data, columns=['Count divides', 'deltaK', 'delta exact', 'sum', 'delta Runge', 'delta teorhy'])


# In[ ]:


df




