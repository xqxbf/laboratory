# w文件异常处理

import os

print("当前目录下的文件：")
os.system("dir" if os.name == 'nt' else "ls")

filename = input("请输入文件名：")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("文件内容：\n", content)
except FileNotFoundError:
    print("错误：文件不存在！")
except PermissionError:
    print("错误：没有权限读文件！")
except UnicodeDecodeError:
    print("错误：文件编码格式不支持！")
except Exception as e:
    print(f"发生未知错误：{type(e).__name__}: {e}")