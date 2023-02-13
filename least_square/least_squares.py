import numpy as np
import matplotlib.pyplot as plt


#テストデータ作成
def data_create(x_min,x_max,N):
    x = np.linspace(x_min,x_max,N)
    y = x + (np.random.randn(N) * 150)
    return x,y

def calculate_regression(x,y):
    x_mean = x.mean()
    y_mean = y.mean()
    #xとyの共分散
    covariance = ((x - x_mean) * (y - y_mean)).sum() / N

    #xの分散
    x_variance = ((x - x_mean) ** 2).sum() / N

    #傾き = 共分散 / xの分散
    slope = covariance / x_variance

    #切片 = yの平均 - （傾き * xの平均）
    intercept = y_mean - (slope * x_mean)

    #y = ax + b
    regression_y = (slope * x) + intercept

    return regression_y


x_min = 0
x_max = 1000
N = 70

x,y = data_create(x_min,x_max,N)
plt.scatter(x,y)

regression_y = calculate_regression(x,y)
plt.plot(x,regression_y,c='red')

plt.show()