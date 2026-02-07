#使用列表推导式创建各种列表

#创建1-10的平方列表
squares = [x**2 for x in range(1, 11)]
print("平方列表：", squares)

#只包含偶数的平方
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("偶数平方列表：", even_squares)

#矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("转置矩阵：", transposed)