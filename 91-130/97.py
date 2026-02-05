# 统计文本文件的行数、单词数、字符数

import os
import sys
import time

def get_file():
    """获取待统计的文本文件"""
    print("当前文件夹下的文件有：")
    count = 1
    for item in os.listdir():
        if os.path.isfile(item):
            print(f"{count}. {item}")
            count += 1
    print()
    file_name = input("请输入待统计的文本文件：")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("错误：请确认文件是否存在或输入的文件名是否有误！")
        return None
    except Exception as e:
        print(f"读取文件时出错：{type(e).__name__}, {e}")
        return None
    else:
        return content
    
def count_file():
    """
    统计文本文件的行数、单词数、字符数
    要求：文件必须存在，且编码为utf-8
    """
    content = get_file()
    if content is None:
        return
    lines = content.splitlines()
    words = content.split()
    chars = len(content)
    print(f"该文件共有{len(lines)}行，{len(words)}个单词，{chars}个字符")

count_file()
