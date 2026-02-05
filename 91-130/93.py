# 异常处理基础

try:
    """可能触发异常的代码"""
    num1 = float(input("请输入被除数："))
    num2 = float(input("请输入除数："))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
except ZeroDivisionError:
    print("错误，除数不能为零！")
except ValueError:
    print("错误，请输入有效的数字！")
except Exception as e:
    print(f"发生未知错误：{e}")
else :
    print("计算成功")
finally:
    print("程序执行结束")