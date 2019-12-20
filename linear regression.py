import numpy as np
from numpy import dot
from decimal import Decimal

X = np.array([[1, 1], [1, 2], [1, 3]]).reshape(3, 2)  # x为1,2,3 前面的是X0，作为纵截距的
Y = np.array([5, 10, 15])  # y为5,10,15

theta = np.array([1.0,1.0]) #初始为1，注意这个浮点数
alpha = 0.5# 学习率为0.1


def gradient_descent(X, Y, theta, alpha):
    temp = theta.copy()
    for times in range(0, 1000):
        #print("num" + str(times) + ":")
        for i in range(0, 2):
            der = 0
            for j in range(0, 3):
                der = der + (dot(X[j], theta) - Y[j]) * X[j][i]
            temp[i] = theta[i] - alpha * der * 1 / 3
            #print("  theta" + str(i) + ':' + str(theta[i]))
            #print("  der:" + str(der))
            #print(temp)
        theta = temp
        #print("  theta" + str(i) + ':')
        print(times)
        print(theta)
    return theta

def demical_method(theta):
    t1 = Decimal(str(theta[0])).quantize(Decimal('0.00'))
    t2 = Decimal(str(theta[1])).quantize(Decimal('0.00'))
    theta1 = np.array([t1,t2])
    return theta1


theta = gradient_descent(X,Y,theta,alpha)

theta = demical_method(theta)

print(theta)