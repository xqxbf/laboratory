# 将一个文件复制到另一个文件
import os
import shutil

def file_copy():
    """文件复制"""

    """当前目录下的文件"""
    count = 1
    for item in os.listdir():
        if os.path.isfile(item):
            print(f"{count}. {item}")
            count += 1

    """设定文件来源去向"""
    from_path_file = input("请输入要待操作的文件的文件名：")
    option = int(input("请输入操作选项（1. 查看    2. 复制）："))
    if option == 1:
        try:
            with open(from_path_file, 'r', encoding='utf-8') as file:
                print("文件内容：")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("错误：文件不存在！")
        except PermissionError:
            print("错误：没有权限读取文件！")
        except UnicodeDecodeError:
            print("错误：文件编码格式不支持！（目前仅支持utf-8编码）")
        except Exception as e:
            print("发生未知错误：", type(e).__name__)
    elif option == 2:
        to_path = input("请输入该文件要复制到的文件路径（若不指定则默认复制到当前目录）：")
        if not to_path:
            to_path = os.getcwd()
        count = 1
        if from_path_file in os.listdir(to_path):
            print("错误：目标目录下已存在同名文件！")
            option = int(input("请输入操作选项（1. 查看已存在的同名文件    2. 另存为一个新文件    3. 直接覆盖原文件    4. 取消操作）："))
            if option == 1:
                try:
                    with open(os.path.join(to_path, from_path_file), 'r', encoding='utf-8') as file:
                        print("已存在的同名文件内容：")
                        for line in file:
                            print(line.strip())
                except FileNotFoundError:
                    print("错误：文件不存在！")
                except PermissionError:
                    print("错误：没有权限读取文件！")
                except UnicodeDecodeError:
                    print("错误：文件编码格式不支持！（目前仅支持utf-8编码）")
                except Exception as e:
                    print("发生未知错误：", type(e).__name__)
            elif option == 2:
                new_file_name = input("请输入新文件名：")
                shutil.copy(from_path_file, os.path.join(to_path, new_file_name))
                print("文件复制完成")
            elif option == 3:
                shutil.copy(from_path_file, os.path.join(to_path, from_path_file))
                print("文件复制完成")
            elif option == 4:
                print("操作已取消")
            else:
                print("错误：无效的操作选项！")

        else:
            shutil.copy(from_path_file, to_path)
            print("文件复制完成")
            



file_copy()