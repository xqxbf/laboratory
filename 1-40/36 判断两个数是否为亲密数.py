#判断两个数是否为亲密数
tmp1 = num1 = int(input("请输入第一个整数："))
tmp2 = num2 = int(input("请输入第二个整数："))
sum1 = sum2 = 1
while tmp1 != 1:
    for i in range(2, tmp1+1) :
        if tmp1 % i == 0 :
            sum1 += i
            tmp1 //= i
sum1 -= num1

while tmp2 != 1:
    for i in range(2, tmp2+1) :
        if tmp2 % i == 0 :
            sum2 += i
            tmp2 //= i
sum2 -= num2

if sum1 == num2 and sum2 == num1:
    print(f"{num1}和{num2}是亲密数")
else:
    print(f"{num1}和{num2}不是亲密数")
