#判断一个数是否为素数
num = int(input("请输入一个整数："))
if num <= 1:
    is_prime =False
else :
    is_prime = True
    for i in range(2, int(num ** 0.5 +1)):
        if num % i == 0 :
            is_prime = False
            break

if is_prime:
    print(f"{num}是素数")
else :
    print(f"{num}不是素数")
