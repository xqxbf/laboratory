#判断一个数是否等于其所有真因子之和
num = int(input("请输入一个整数："))

sum = 0
for i in range(1,num):
    if num % i == 0 :
        sum += i

if sum == num :
    print(f"{num}是一个完数")
else :
    print(f"{num}不是一个完数")