#输入n个数，求它们的和（while循环)
n = int(input("请输入n: "))
i = 1
sum = 0
while i <= n:
    num = int(input(f"请输入第{i}个数："))
    sum += num
    i += 1
print(f"这{n}个数的和是：{sum}")