# 长度、重量、温度单位转换

import os
import time
import sys

def length_convert(length, unit):
    """长度单位转换函数"""
    if unit == "m": 
        print(length, "m =", length * 100, "cm")
        print(length, "m =", length * 1000, "mm")
    elif unit == "cm":
        print(length, "cm =", length / 100, "m")
        print(length, "cm =", length * 10, "mm")
    elif unit == "mm":
        print(length, "mm =", length / 1000, "m")
        print(length, "mm =", length / 10, "cm")
        return 1

def weight_convert(weight, unit):
    """重量单位转换函数"""
    if unit == "kg":
        print(weight, "kg =", weight * 1000, "g")
        print(weight, "kg =", weight * 1000000, "mg")
    elif unit == "g":
        print(weight, "g =", weight / 1000, "kg")
        print(weight, "g =", weight * 1000, "mg")
    elif unit == "mg":
        print(weight, "mg =", weight / 1000000, "kg")
        print(weight, "mg =", weight / 1000, "g")
        return 1

def temp_convert(temp, unit):
    """温度单位转换函数"""
    if unit == "℃":
        print(temp, "℃ =", temp * 9 / 5 + 32, "℉")
    elif unit == "℉":
        print(temp, "℉ =", (temp - 32) * 5 / 9, "℃")
        return 1

def get_number_and_unit(correct):
    """获取用户输入的数值和单位"""
    number_part = ""
    unit_part =""

    for char in correct:
        if char.isdigit() or char == ".":
            number_part += char
        else:
            unit_part += char

    if number_part:
        number = float(number_part)
    else:
        number = None
        
    unit = unit_part.strip().lower()

    return number, unit

os.system("cls" if os.name == "nt" else "clear")

length_unit = ["m", "cm", "mm"]
weight_unit = ["kg", "g", "mg"]
temp_unit = ["℃", "℉"]

print("~o( =∩ω∩= )m > 欢迎使用长度单位转换工具！")
print()
print("请输入当前变量值（已支持长度、重量、温度单位,如：100m, 200kg, 300℃）：", end="")
number, unit = get_number_and_unit(input())
if number is None:
    print("似乎存在问题，考虑一下检查输入是否正确呗。")
    time.sleep(2)
    sys.exit(0)

if unit in length_unit:
    result = length_convert(number, unit)
elif unit in weight_unit:
    result = weight_convert(number, unit)
elif unit in temp_unit:
    result = temp_convert(number, unit)
else:
    print("似乎存在问题，考虑一下检查输入是否正确呗。")
    time.sleep(2)
    sys.exit(0)

if result:
    print("执行成功，2秒后自动退出")
    time.sleep(2)
    sys.exit(0)


