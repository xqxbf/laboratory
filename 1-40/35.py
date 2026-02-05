#将一个正整数分解为质因数
num = int(input("请输入一个整数："))
print(f"{num} = 1 ", end=' ')

while num != 1:
    for i in range(2, num+1) :
        if num % i == 0:
            num = num // i
            print(f"* {i}", end=' ')
            break
