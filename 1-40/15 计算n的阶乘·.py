#计算n的阶乘·
n = int(input("请输入一个非负整数："))
factorial = 1
for i  in range(1, n+1):
    factorial += i
print(f"{n}! = {factorial}")