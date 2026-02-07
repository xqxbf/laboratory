# 实现凯撒密码加密、解密

import sys
import time
import os

def time_count(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"加密成功，执行时间: {execution_time:.6f} 秒")
        return result
    return wrapper

@time_count
def encryption(text, shift):
    encrypted_text = ""
    for char in text:
        new_char = chr(ord(char) + shift)
        encrypted_text += new_char
    return encrypted_text


passwd = input("请输入待加密文本（exit退出）：")
if passwd == "exit":
    sys.exit(0)

try:
    shift_input = input("请输入凯撒值（+）：")
    if shift_input == "":
        shift = 4
        print("未检测到新的凯撒值")
    else:
        shift = int(shift_input)
except ValueError:
    shift = 4
    print("输入无效，使用默认值4")

print(f"即将加密值：{passwd}，更新后的凯撒值：{shift}，是否继续？（Y/n）", end="")

option = input()
if option == 'y' or option == '' or option == 'Y':
    os.system("cls" if os.name == "nt" else "clear")
    new_passwd = encryption(passwd, shift)
    print(f"加密后的文本：{new_passwd}")
else :
    os.system("cls" if os.name == "nt" else "clear")
    print("操作被取消，2秒后退出程序")
    time.sleep(2)
