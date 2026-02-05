#输出斐波那契数列的前n项
n = int(input("请输入项数："))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
