import math

a = 11
b = -0.4
c = 1
d = 0.21
eps = 0.0001


def findMinGradFunction():
    x = [0]
    y = [0]
    dx = {}
    dy = {}
    alphaK = 1
    
    z = x[0] + y[0] + math.exp(c * x[0] ** 2 + d * y[0] ** 2)
    
    while True:
        x[x.count()] = x[x.count()-1] - alphaK*dx[x[x.count()-1]]
        y[y.count()] = y[y.count()-1] - alphaK*dy[y[y.count()-1]]
        
        if(getValue(x[x.count()], y[y.count()]) > getValue(x[x.count()], y[y.count()])):
        



def getValue(x,y):
    z = x + y + math.exp(c * x ** 2 + d * y ** 2)
    return z
   
 
if __name__ == '__main__':
    findMinGradFunction()
