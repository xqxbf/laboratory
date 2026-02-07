#实现3x3矩阵的加法和乘法
import math

num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum1 = 0
result = 1

sum1 = sum(num[i][j] for i in range(3) for j in range(3))
print("矩阵所有元素和：", sum1)

result = math.prod(num[i][j] for i in range(3) for j in range(3))
print("矩阵所有元素积：", result)