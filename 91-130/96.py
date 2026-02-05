# 合并多个文本文件

import os
import sys
import time

def get_file_list() -> list:
    """获取待合并的文本文件"""
    file_list = []
    
    """输出该目录下的文件"""
    count = 1
    for item in os.listdir():
        if os.path.isfile(item):
            print(f"{count}. {item}")
            count += 1

    """获得待合并的文本文件"""
    count = 0
    print("请依次输入待合并的文本文件，可输入exit退出: ")
    while True:
        file_name = input("请输入: ")
        if file_name == "" or file_name.isspace() or file_name == "exit":
            break
        try:
            with open(file_name, "r") as file:
                file_list.append(file_name)
        except FileNotFoundError:
            print("文件不存在")
        except Exception as e:
            print(f"未知错误: {e}")

    """确定后返回"""
    if len(file_list) == 0:
        print("未选择任何文件，2秒后程序退出")
        time.sleep(2)
        sys.exit(0)
    else :
        print("已选择的文件：")
        for item in file_list:
            print(item, end='  ')
        print('\n')
        return file_list

def append_file_content() -> None:
    """合并文件内容"""
    file_list = get_file_list()
    with open("merged.txt", "w") as merged_file:
        for file_name in file_list:
            with open(file_name, "r") as file:
                merged_file.write(file.read())
                merged_file.write("\n\n")

append_file_content()