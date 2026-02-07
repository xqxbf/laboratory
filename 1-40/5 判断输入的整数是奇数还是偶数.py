#判断输入的整数是奇数还是偶数
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print(f"{num}是一个偶数")
else:
    print(f"{num}是一个奇数")