# 支持多种运算的计算机函数

import os 
import time
import sys

def title():
    """显示标题"""
    print("         ***************************************")
    print("         ***                                 ***")
    print("         ***              计算器             ***")
    print("         ***                                 ***")
    print("         ***************************************")
    print()

def clean_screen_with_title():
    """清屏并显示标题"""
    os.system("cls" if os.name == "nt" else "clear")
    title()

def calculate():
    """计算函数"""
    clean_screen_with_title()
    print("~o( =∩ω∩= )m > 请输入第一个操作数：", end="")
    num1 = float(input())
    print("~o( =∩ω∩= )m > 请输入运算符(+/-/*//)：", end="")
    operator = input()
    if operator not in ["+", "-", "*", "//"]:
        clean_screen_with_title()
        print("~o( =∩ω∩= )m > 输入无效，请重新输入！")
        continue_calculate()
        return

    print("~o( =∩ω∩= )m > 请输入第二个操作数：", end="")
    num2 = float(input())
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "//":
        result = num1 // num2

    clean_screen_with_title()
    print("~o( =∩ω∩= )m > 计算结果为：", result)
    continue_calculate()

def continue_calculate():
    """继续计算函数"""
    print("~o( =∩ω∩= )m > 是否继续计算？(Y/n)：", end="")
    choice = input()
    if choice == "Y" or choice == "y" or choice == "":
        calculate()
    else:
        clean_screen_with_title()
        print("~o( =∩ω∩= )m > 谢谢使用！")
        time.sleep(2)
        sys.exit()

calculate()
