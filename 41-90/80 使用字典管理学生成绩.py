# 使用字典管理学生成绩
import os
import time

def clear_screen():
    """清屏函数，兼容不同操作系统"""
    os.system('cls' if os.name == 'nt' else 'clear')

student = {
    "姓名": "梓潼",
    "成绩": {
        "语文": 90,
        "数学": 85,
        "英语": 88,
        "科学": 92,
    }   
}

print("请输入操作选项：\n1.查询成绩 \n2.添加成绩 \n3.修改成绩 \n4.删除成绩 \n5.退出 \n请输入：", end="")
while True :
    option = int(input())

    # 清屏
    clear_screen()

    if option == 1:
        print(f"{student['姓名']}的成绩如下：")
        for subject, score in student["成绩"].items():
            print(f"{subject}：{score}")

    elif option == 2:
        subject = input("请输入要添加的科目：")
        score = int(input("请输入该科目的成绩："))
        student["成绩"][subject] = score
        print("成绩添加成功，当前成绩如下：")
        for subject, score in student["成绩"].items():
            print(f"{subject}：{score}")

    elif option == 3:
        subject = input("请输入要修改的科目：")
        if subject in student["成绩"]:
            score = int(input("请输入该科目的新成绩："))
            student["成绩"][subject] = score
            print("成绩修改成功，当前成绩如下：")
            for subject, score in student["成绩"].items():
                print(f"{subject}：{score}")
        else:
            print("该科目不存在")

    elif option == 4:
        subject = input("请输入要删除的科目：")
        if subject in student["成绩"]:
            del student["成绩"][subject]
            print("成绩删除成功，当前成绩如下：")
            for subject, score in student["成绩"].items():
                print(f"{subject}：{score}")
        else:
            print("该科目不存在")

    elif option == 5:
        print("程序已注销，5秒后返回")
        time.sleep(5)
        break

    else:
        print("无效选项，请重新输入")

    # 清屏
    clear_screen()

    print("任务完成，请输入下一步操作：", end="")
