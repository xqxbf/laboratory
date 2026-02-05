#反转一个整数
num = int(input("请输入一个整数："))
resersed_num = int(str(abs(num))[::-1]) #字符串切片反转
if num < 0:
    resersed_num = -resersed_num
print(f"反转后: {resersed_num}")