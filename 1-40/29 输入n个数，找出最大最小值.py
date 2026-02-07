#输入n个数，找出最大最小值
n = int(input("请输入整数的个数："))

max = int(input("请输入第一个整数："))
min = max

for i in range(1,n):
    num = int(input("请输入第%d个整数："%(i+1)))
    if num > max :
        max = num
    if num < min :
        min = num
print(f"最大数为{max}，最小数为{min}")
