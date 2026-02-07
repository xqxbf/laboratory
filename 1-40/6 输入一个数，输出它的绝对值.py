#输入一个数，输出它的绝对值
num = float(input("请输入一个整数:"))
abs_value = num if num >= 0 else -num
print(f"{num}的绝对值是{abs_value}")