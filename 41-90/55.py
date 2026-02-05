#用递归实现阶乘计算
def factorial(n):
    if n== 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("请输入一个非负整数："))))