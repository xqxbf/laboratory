# 编写模块的模块字符串(调用前请在文件名前面加上_)

"""
这是一个简单的计算机模块

功能：
- 加法
- 减法
- 乘法
- 除法

使用方法：
1. 导入模块：`import computer`
2. 使用函数：`result = computer.add(1, 2)`
"""

def add(a, b):
    """
    加法函数
    """
    return a + b

def sub(a, b):
    """
    减法函数
    """
    return a - b

def mul(a, b):
    """
    乘法函数
    """
    return a * b

def div(a, b):
    """
    除法函数
    """
    return a / b

