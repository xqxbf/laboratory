# 演示字典的增删改查

student = {
    "姓名": "梓潼",
    "年龄": 18,
    "性别": "男",
    "班级": "25级3班"
}

print("初始字典:", student)

# 增：添加新键值对
student["成绩"] = 95

# 删：删除指定键
del student["性别"]

# 改：更新已有键的值
student["年龄"] = 19

# 查：访问并打印某个键的值
print("姓名:", student["姓名"])
print("完整字典:", student)
