 #用*打印等腰三角形
n = int(input("请输入层数："))
for i in range(0, n):
    print(" " * (n-i-1), end='')
    print("*" * (2*i+1))
    