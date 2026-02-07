# 计算机生成数字，用户猜

import random
import time
import sys
import os

os.system("cls" if os.name == "nt" else "clear")

def show_title():
    """显示标题框"""
    print("         ***************************************")
    print("         ***                                 ***")
    print("         ***              猜数字             ***")
    print("         ***                                 ***")
    print("         ***************************************")
    print()

def clear_screen_with_title():
    """清屏并显示标题"""
    os.system("cls" if os.name == "nt" else "clear")
    show_title()

while True:
    """主程序"""
    correct_num = random.randint(1, 100)
    clear_screen_with_title()
    print("你好，欢迎来到来数字环节，我已经为你准备好了一个1到100中的数，看试试你需要几次才能猜到它！")
    print("准备好了吗？（Y/n）：", end="")
    choice = input()
    if choice == "Y" or choice == "y" or choice == "":
        """游戏开始"""
        while True:
            count = 1
            has_num = []
            while True:
                may_num = input(f"第{count}次：")

                """中途退出"""
                if may_num == "exit":
                    print("你还是放弃了吗？（Y/n）", end="")
                    choice = input()
                    if choice == "Y" or choice == "y" or choice == "":
                        """确认退出"""
                        print("好吧，再见！2秒后退出程序")
                        time.sleep(2)
                        sys.exit(0)
                    elif choice == "N" or choice == "n":
                        """取消退出"""
                        print("什么？你竟然没有放弃！（╯‵□′）╯︵┻━┻(按Enter继续吧)")
                        input()
                        clear_screen_with_title()
                        print("太好了！加油哦！")
                    else :
                        """异常输入"""
                        print("我看不懂诶(。>︿<)_θ，能重新输入吗？（Y/n）", end="")
                        choice = input()
                        if choice == "Y" or choice == "y" or choice == "":
                            print("什么？你竟然没有放弃！（╯‵□′）╯︵┻━┻(按Enter继续吧)")
                            input()
                            clear_screen_with_title()
                            print("太好了！加油哦！")
                        else:
                            print("好吧，再见！2秒后退出程序")
                            time.sleep(2)
                            sys.exit(0)
                else:
                    """输入非整数情况"""
                    try:
                        may_num = int(may_num)
                    except ValueError:
                        print("啊？不是要输入整数嘛？o(≧口≦)o")
                        continue

                    """输入整数情况"""
                    if may_num in has_num:
                        print("你之前猜过这个数字了，尊都！(*≧︶≦))(￣▽￣* )ゞ")
                        continue
                    has_num.append(may_num)

                    """给出判断"""
                    clear_screen_with_title()
                    print(f"你猜的数字是{may_num}. ", end="")
                    if may_num == correct_num:
                        print(f"Great! 你用了{count}次", end='')
                        if count == 1:
                            print("，just one!")
                        elif count > 1 and count <= 6:
                            print("，not bad!")
                        else:
                            print("，try harder!")
                        print("2秒后退出程序")
                        time.sleep(2)
                        sys.exit(0)
                    elif may_num > correct_num:
                        print("数字太大了")
                    else:
                        print("数字太小了")
                    
                    if count == 1:
                        print("别急,我偷偷帮你记住了所有的你输入的数: ", end="")
                    else:
                        print("所有的数: ", end="")
                    print(has_num)
                    
                    count += 1
    
    else:
        """在开始时退出"""
        print("￣へ￣", end='    ')
        print("那下次叭")
        sys.exit(0)
