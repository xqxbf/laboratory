# 求解二元一次方程组

import os
import sys
import time
import numpy as np

def get_equation(equation_num):
    """获取二元一次方程组的系数"""
    print(f"请输入第{equation_num}个方程组的系数A、B、C")
    while True:
        try:
            A = float(input("A = "))
            B = float(input("B = "))
            C = float(input("C = "))
            break
        except ValueError:
            print("请输入正确的数值")
    return A, B, C

def calculate():
    """计算方程组的解"""
    A1, B1, C1 = get_equation(1)
    A2, B2, C2 = get_equation(2)
    # 构建系数矩阵和常数向量
    A = np.array([[A1, B1], [A2, B2]])
    B = np.array([C1, C2])
    # 求解方程组
    try:
        X = np.linalg.solve(A, B)
        print("方程组的解为：")
        print("x =", X[0])
        print("y =", X[1])
    except np.linalg.LinAlgError:
        print("方程组无解")

def main():
    """主函数"""
    os.system("cls" if os.name == "nt" else "clear")
    print("~o( =∩ω∩= )m > 欢迎使用二元一次方程组求解器")
    print()
    print("请按照Ax + By = C的格式输入方程组的系数A、B、C")
    print("例如：2x + 3y = 10")
    print()
    print("按回车键继续")
    input()
    os.system("cls" if os.name == "nt" else "clear")
    print("~o( =∩ω∩= )m > 欢迎使用二元一次方程组求解器")
    print()
    calculate()


if __name__ == "__main__":
    main()