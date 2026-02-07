#计算两个数的最大公约数
a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))

#欧几里得算法
while b:
    a, b = b, a % b
print(f"最大公约数为: {a}")