# 合并多个字典的方法

student1 = {
    "姓名": "梓潼",
    "年龄": 18,
    "性别": "男",
    "班级": "25级3班"
}

student2 = {
    "科目": "数学",
    "成绩": 95
}

# 合并字典
student = {**student1, **student2}
print(' \n'.join(f"键: {k}, 值: {v}" for k, v in student.items()))
