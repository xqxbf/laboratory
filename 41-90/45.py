#去除列表中的重复元素
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print("去重后的列表：", unique_numbers)
