# 使用集合对列表去重

original_list = [1, 2, 2, 3, 4, 4, 5]  # 原始列表

unique_list = list(set(original_list))  # 去重后的列表
print("去重后的列表:", unique_list)
