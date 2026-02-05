#输入10个数，统计正负数和零的个数
positive = negative = zero = 0
for i in range(10):
    num = float(input(f"请输入第{i+1}个数："))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else :
        zero += 1
print(f"正数：{positive}，负数：{negative}，零：{zero}")