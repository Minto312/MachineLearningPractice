import numpy as np
import matplotlib.pyplot as plt
import time

#テストデータ作成
def data_create(x_min,x_max,N):
    x = np.linspace(x_min,x_max,N)
    y = x + (np.random.randn(N) * 150)
    return x,y

def calculate_regression_insidemean(x,y):
    #xとyの共分散
    covariance = ((x - x.mean()) * (y - y.mean())).sum() / N

    #xの分散
    x_variance = ((x - x.mean()) ** 2).sum() / N

    #傾き = 共分散 / xの分散
    slope = covariance / x_variance

    #切片 = yの平均 - （傾き * xの平均）
    intercept = y.mean() - (slope * x.mean())

    #y = ax + b
    regression_y = (slope * x) + intercept

    return regression_y

def calculate_regression_outsidemean(x,y):
    x_mean = x.mean()
    y_mean = y.mean()
    #xとyの共分散
    covariance = ((x - x_mean) * (y - y_mean)).sum()

    #xの分散
    x_variance = ((x - x_mean) ** 2).sum() / N

    #傾き = 共分散 / xの分散
    slope = covariance / x_variance

    #切片 = yの平均 - （傾き * xの平均）
    intercept = y_mean - (slope * x_mean)

    #y = ax + b
    regression_y = (slope * x) + intercept

    return regression_y
total = 0
repeat = 30000

x_min = 0
x_max = 1000
N = 100000
for i in range(repeat):
    start = time.perf_counter()
    x,y = data_create(x_min,x_max,N)

    regression_y = calculate_regression_insidemean(x,y)

    total += time.perf_counter() - start
    print(f'\r{i}/{repeat}',end='')
inside_score = total
print(f'\n inside_ver : {inside_score}\n\n')

total = 0
for i in range(repeat):
    start = time.perf_counter()
    x,y = data_create(x_min,x_max,N)

    regression_y = calculate_regression_outsidemean(x,y)

    total += time.perf_counter() - start
    print(f'\r{i}/{repeat}',end='')
outside_score = total
print(f'\n outside_ver : {outside_score}\n\n')

if inside_score < outside_score:
    print(f'inside is {outside_score - inside_score} fast')
else:
    print(f'outside is {inside_score - outside_score} fast')