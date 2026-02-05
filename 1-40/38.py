#找出小于n的最大平方数

n = int(input("请输入一个整数："))

for i in range(1, n+1):
    if i * i < n:
        max_square = i * i

print(f"小于{n}的最大平方数为：{max_square}")
