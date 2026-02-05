#根据分数输出等级
score = float(input("请输入成绩（1-100）："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else :
    grade = 'E'
print(grade)