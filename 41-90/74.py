# 按键或按值对字典排序

student = {
    "姓名": "梓潼",
    "年龄": 18,
    "性别": "男",
    "班级": "25级3班",
    "科目": "数学",
    "成绩": 95
}

# 按键排序
sorted_by_key = dict(sorted(student.items()))
print("按键排序:", sorted_by_key)

# 按值排序（处理不同类型的值）
sorted_by_value = dict(sorted(student.items(), key=lambda item: (type(item[1]).__name__, item[1])))
print("按值排序:", sorted_by_value)