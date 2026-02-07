# 实现添加、删除、查找联系人

import os
import time

contact = {}    # 初始化字典

# 添加
def add_contact(name, phone="", email="", address="") :
    if name in contact :
        print("该联系人已存在")
    else :
        contact[name] = {
            "电话" : phone,
            "邮箱" : email,
            "地址" : address
        }
        print("操作执行成功")

# 删除
def del_contact(name) :
    if name in contact :
        del contact[name]
        print("操作执行成功")
    else :
        print("该联系人不存在")

# 查找
def find_contact(name) :
    if name in contact :
        print(f"{name}的信息如下：")
        for key, value in contact[name].items() :
            print(f"{key}: {value}")
        print("操作执行成功")
    else :
        print("该联系人不存在")

# 清屏
def clear_screen() :
    os.system("cls" if os.name == "nt" else "clear")

# 主函数
if __name__ == "__main__" :
    while True :
        # 显示菜单
        print("请输入操作选项：")
        print("1.添加联系人")
        print("2.删除联系人")
        print("3.查找联系人")
        print("4.退出")
        print("请输入：", end="")

        try:
            option = int(input())
        except ValueError:
            print("错误：请输入数字选项！")
            input("按回车键继续...")
            clear_screen()
            continue

        # 清屏
        clear_screen()

        if option == 1:
            name = input("请输入联系人姓名：")
            if name == "exit" :
                continue
            phone = input("请输入联系人电话（可选）：")
            if phone == "exit" :
                continue
            email = input("请输入联系人邮箱（可选）：")
            if email == "exit" :
                continue
            address = input("请输入联系人地址（可选）：")
            if address == "exit" :
                continue
            add_contact(name, phone, email, address)
            input("按回车键继续...")
            clear_screen()

        elif option == 2:
            name = input("请输入要删除的联系人姓名：")
            if name == "exit" :
                continue
            del_contact(name)
            input("按回车键继续...")
            clear_screen()

        elif option == 3:
            for name, info in contact.items():
                find_contact(name)
            input("按回车键继续...")
            clear_screen()

        elif option == 4:
            print("程序已注销，2秒后退出")
            time.sleep(2)
            break

        else:
            print("无效选项，请重新输入")
            input("按回车键继续...")
            clear_screen()