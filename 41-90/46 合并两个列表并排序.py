#合并两个列表并排序
list1 = [3, 1, 4]
list2 = [1, 5, 9]
merged = sorted(list1 + list2)
result = list(set(merged))
print("合并并排序后的列表：", result)
