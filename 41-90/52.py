#创建一个带默认参数的问候函数
def greet(name = "Guest"):
    if name.strip() == "":
        name = "Guest"
    print("你好，" + name + "!")

#调用greet函数，传递参数
name = input("请输入你的姓名：")
greet(name)
