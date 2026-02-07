# 计算两个日期中间的时间差

import datetime as dt
import os
import time
import sys

def get_time():
    """获取时间函数"""
    try:
        date = dt.datetime.strptime(input(), "%Y-%m-%d")
        return date
    except ValueError:
        print("似乎存在问题，考虑一下检查输入的月份和日期是否正确呗。")
        time.sleep(2)
        sys.exit(0)
    

os.system("cls" if os.name == "nt" else "clear")
print("~o( =∩ω∩= )m > 欢迎使用时间差计算器！")
print()
print("请输入第一个时间(YYYY-MM-DD)：", end="")
date1 = get_time()
print("请输入第二个时间(YYYY-MM-DD)：", end="")
date2 = get_time()
time_difference = date2 - date1
print("两个日期之间的时间差为：", abs(time_difference.days), "天")

    
