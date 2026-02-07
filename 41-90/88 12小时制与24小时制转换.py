# 12小时制与24小时制转换

import os
import time
import sys
import datetime as dt

def time_print(input_time, option):
    """时间打印函数"""
    os.system("cls" if os.name == "nt" else "clear")
    if option == 1:
        print(input_time, "的24小时制时间为：", input_time.strftime("%H:%M:%S"))
    elif option == 2:
        print(input_time, "的12小时制时间为：", input_time.strftime("%I:%M:%S %p"))
    print("执行成功，2秒后自动退出")
    time.sleep(2)
    sys.exit(0)

os.system("cls" if os.name == "nt" else "clear")
print("~o( =∩ω∩= )m > 欢迎使用时间转换工具！")
print()
print("请输入时间(HH:MM:SS)(记得冒号是英文冒号哦)：", end="")
time_str = input()
try:
    time_obj = dt.datetime.strptime(time_str, "%H:%M:%S")
    option = int(input("请选择转换选项\n1:24小时制\n2:12小时制\n请输入："))
    if option not in [1, 2]:
        print("似乎存在问题，考虑一下检查输入的选项是否正确呗。")
        time.sleep(2)
        sys.exit(0)
    else :
        time_print(time_obj, option)
except ValueError:
    print("似乎存在问题，考虑一下检查输入的时间是否正确呗。")
    time.sleep(2)
    sys.exit(0)
