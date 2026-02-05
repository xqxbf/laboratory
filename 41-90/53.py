#创建接受任意数量参数的求和函数

def max_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

user_input = input("请输入任意个整数：")
numbers = [float(num.strip()) for num in user_input.split()]
#解包传给函数
result = max_all(*numbers)
print("这些数的和为", result)