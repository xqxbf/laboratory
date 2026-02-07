# 处理学生成绩csv文件

import csv
import os
import time
import sys
import openpyxl

if __name__ == '__main__':
    # 检查目录下的csv文件
    os.system('cls' if os.name == 'nt' else 'clear')

    count = 1
    print("当前目录下的csv文件：")
    for item in os.listdir():
        if os.path.isfile(item) and item.endswith('.csv'):
            print(f"{count}. {item}")
            count += 1

    try:
        choice = int(input("请输入要处理的文件编号："))
    except ValueError:
        print("输入错误，请输入一个整数")
        sys.exit(1)
    if choice < 1 or choice >= count:
        print("无效的选择")
        sys.exit(1)
        
    selected_file = os.listdir()[choice - 1]
    print(f"已选择文件：{selected_file}")

    try:
        # 读取csv文件
        with open(selected_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)

    except FileNotFoundError:
        print(f"错误：文件 {selected_file} 不存在")
    except PermissionError:
        print(f"错误：没有权限读取文件 {selected_file}")
    except csv.Error as e:
        print(f"CSV文件读取错误：{e}")
    except Exception as e:
        print(f"未知错误：{e}")
    else:
        while True:
            operation = int(input("请选择操作：1. 读取 2. 写入 3.修改 4.备份 5.退出"))
            if operation == 1:
                with open(selected_file, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            elif operation == 2:
                print("注意：当前写操作仅支持导入excel文件内容")
                wb = input("请输入要导入的excel文件路径：")
                try:
                    wb = openpyxl.load_workbook(wb)
                    ws = wb.active
                except FileNotFoundError:
                    print(f"错误：文件 {wb} 不存在")
                    continue
                except PermissionError:
                    print(f"错误：没有权限读取文件 {wb}")
                    continue
                except Exception as e:
                    print(f"未知错误：{e}")
                    continue
                with open(selected_file, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(ws.values)
                    print("写入完成")
            elif operation == 3:
                with open(selected_file, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                print(lines)
                line_key = input("请输入要修改的键：")
                if line_key not in lines[0]:
                    print("键不存在")
                    continue
                else :
                    line_value = input("请输入要修改的值：")
                    lines[0] = lines[0].replace(line_key, line_value)
                    with open(selected_file, 'w', encoding='utf-8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(lines)
                        print("修改完成")
            elif operation == 4:
                backup_file = selected_file.split('.')[0] + '_backup.csv'
                with open(backup_file, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(lines)
                print("备份完成")
            elif operation == 5:
                print("退出程序")
                break
            else:
                print("无效的选择")
        print("请选择操作：1. 读取 2. 写入 3.修改 4.备份 5.退出")
