#统计整数各位数字中奇数偶数的个数
num = int(input("请输入一个整数："))

odd = 0
even = 0

while num != 0:
    digit = num % 10
    if digit % 2 == 0:
        even += 1
    else :
        odd += 1
    num //= 10

print(f"该整数中共有{odd}个奇数，{even}个偶数")