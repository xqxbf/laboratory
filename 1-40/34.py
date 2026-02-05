#输入n个数，求最大连续子序列和
n = int(input("请输入整数的个数："))

max_sum = int(input("请输入第一个整数："))
current_sum = max_sum

for i in range(1,n):
    num = int(input("请输入第%d个整数："%(i+1)))
    if current_sum < 0:
        current_sum = num
    else:
        current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
print(f"最大连续子序列和为：{max_sum}")

