#计算两个数的最小公倍数
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))

#先求最大公约数
x, y = a, b
while y:
    x, y = y, x % y
gcd = x

#最小公倍数 = a * b /最大公约数
lcm = a * b // gcd
print(f"最小公倍数是：{lcm}")
