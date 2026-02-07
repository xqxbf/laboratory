# 读取CSV格式的数据文件

import csv
import time
import os
import sys

def read_CSV():
    """
    读取CSV文件
    要求：文件必须存在，且编码为utf-8
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    count = 1
    print("当前目录下的csv文件：")
    for item in os.listdir():
        if os.path.isfile(item) and item.endswith('.csv'):
            print(f"{count}. {item}")
            count += 1
    
    print()
    data = []
    file_name = input("请输入待读取的csv文件(输入exit退出)：")
    if file_name == '' or file_name.isspace() or file_name == "exit":
        print("未选择任何文件，2秒后程序退出")
        time.sleep(2)
        sys.exit(0)
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for i in csv.reader(file):
                data.append(i)
    except FileNotFoundError:
        print("错误：请确认文件是否存在或输入的文件名是否有误！2秒后自动退出")
        time.sleep(2)
        sys.exit(0)
        
    except Exception as e:
        print(f"读取文件时出错：{type(e).__name__}, {e}\n2秒后自动退出")
        time.sleep(2)
        sys.exit(0)
    else:
        for i in data:
            print(i, end='   ')
        print("操作执行成功，2秒后自动退出")
        time.sleep(2)
        sys.exit(0)

read_CSV()