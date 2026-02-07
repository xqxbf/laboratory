#实现加减乘除运算
a = float(input("请输入第一个数："))
b = float(input("请输入第二个数："))
op = input("请输入运算符(+, -, *, /):")

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0 :
        result = a / b
    else :
        result = "错误：除数不能为零"
else : 
    result = "错误：无效运算符"

print(f"{a} {op} {b} = {result}")