# 创建一个学生信息字典

student = {
    "姓名": "梓潼",
    "年龄": 18,
    "性别": "男",
    "班级": "25级3班"
}

print(student)

print(student["姓名"])
print(student["年龄"])
print(student["性别"])
print(student["班级"])

for key, value in student.items():
    print(f"{key}: {value}")

