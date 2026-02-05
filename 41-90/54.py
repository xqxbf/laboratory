#函数返回多个值(元组)
def get_name_age():
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    return name, age

#调用函数并解包元组
user_name, user_age = get_name_age()
print("你好，" + user_name + "! 你今年" + str(user_age) + "岁。")