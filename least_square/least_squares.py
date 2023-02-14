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

    #x,yの分散
    x_variance = ((x - x_mean) ** 2).sum() / N
    y_variance = ((y - y_mean) ** 2).sum() / N

    #傾き = 共分散 / xの分散
    slope = covariance / x_variance

    #切片 = yの平均 - （傾き * xの平均）
    intercept = y_mean - (slope * x_mean)

    #y = ax + b
    regression_y = (slope * x) + intercept

    
    #相関係数を求める
    #相関係数 = 共分散 / xの標準偏差 * yの標準偏差
    correlation_coefficient = covariance / (np.sqrt(x_variance) * (np.sqrt(y_variance)))

    return regression_y,correlation_coefficient


x_min = 0
x_max = 1000
N = 70

x,y = data_create(x_min,x_max,N)
plt.scatter(x,y)

regression_y,correlation_coefficient = calculate_regression(x,y)
plt.plot(x,regression_y,c='red')

plt.text(x_max,0,s=f'相関係数 : {correlation_coefficient}',ha='right',fontname='MS Gothic')
plt.show()