# 石头剪刀布(人机对战)

import random 
import time
import sys
import os

"""规则制定"""
computer_choice = random.choice(["石头", "剪刀", "布"])
rules = {
    "石头": "剪刀",
    "剪刀": "布",
    "布": "石头"
}

def judge(computer_choice, user_choice):
    """判断游戏结果"""
    if computer_choice == user_choice:
        return "平局"
    elif rules[computer_choice] == user_choice:
        return "你赢了"
    else:
        return "你输了"

def title() :
    """显示标题"""
    print("         ****************************************")
    print("         ***                                  ***")
    print("         ***      石头剪刀布(人机对战)        ***")
    print("         ***                                  ***")
    print("         ****************************************")
    print()

def clean_screen_with_title():
    """清屏并显示标题"""
    os.system("cls" if os.name == "nt" else "clear")
    title()

clean_screen_with_title()
print("~o( =∩ω∩= )m > 欢迎来到石头剪刀布游戏, 准备好后请直接按回车!", end="")
input()
while True:
    """主程序"""
    clean_screen_with_title()
    print("~o( =∩ω∩= )m > 请输入你的选择(石头/剪刀/布)：", end="")
    user_choice = input().strip()
    clean_screen_with_title()
    print(f"~o( =∩ω∩= )m > 你选择了{user_choice}，电脑选择了{computer_choice}，{judge(computer_choice, user_choice)}")
    print("~o( =∩ω∩= )m > 游戏结束，是否继续？(Y/n)：", end="")
    choice = input()
    if choice == "N" or choice == "n":
        """确认退出"""
        clean_screen_with_title()
        print("~o( =∩ω∩= )m > 好吧，再见！2秒后退出程序")
        time.sleep(2)
        sys.exit(0)
    elif choice == "Y" or choice == "y" or choice == "":
        """确认继续"""
        clean_screen_with_title()
        print("~o( =∩ω∩= )m > 太好了！加油哦！")
        time.sleep(1)
        continue
    else:
        """输入错误"""
        clean_screen_with_title()
        print("~o( =∩ω∩= )m > 输入无效，请重新输入！")
        time.sleep(2)
        continue
