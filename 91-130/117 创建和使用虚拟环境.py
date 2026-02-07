# 创建和使用虚拟环境

import os
import subprocess
import time

def venv_activate(venv_name="venv"):
    """
    激活虚拟环境
    """
    try:
        # 构建激活脚本的完整路径
        activate_script = os.path.join(os.getcwd(), venv_name, "Scripts", "Activate.ps1")
        
        if os.path.exists(activate_script):

            print(f"\n正在尝试激活虚拟环境 {venv_name}")
            subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command", f"& '{activate_script}'; powershell.exe"])
        else:
            print(f"激活脚本不存在：{activate_script}")
    except Exception as e:
        print(f"激活虚拟环境失败：{e}")

def venv_create(venv_name="venv"):
    """
    创建虚拟环境
    """
    if os.path.exists(venv_name):
        if os.path.exists(venv_name+"\\Scripts\\activate"):
            if input("该虚拟环境已存在，是否直接激活（y/n）: ").lower() == "y":
                venv_activate(venv_name)
        else:
            print("该文件夹名称已存在，但不是虚拟环境文件夹")
    else:
        try:
            print("正在尝试创建虚拟环境 ", venv_name)
            subprocess.Popen(f"python -m venv {venv_name}", shell=True, stdout=subprocess.PIPE, text=True)
        except:
            print("创建虚拟环境失败，请检查python是否安装正确")
        else:
            print("虚拟环境 ", venv_name, " 创建成功")
            if input("是否立即激活该虚拟环境（y/n）: ").lower() == "y":
                venv_activate(venv_name)

if __name__ == "__main__":
    venv_name = input("请输入您想创建的虚拟环境名称：")
    venv_create(venv_name)

