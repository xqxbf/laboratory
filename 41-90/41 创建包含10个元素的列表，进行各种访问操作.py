#创建包含10个元素的列表，进行各种访问操作
numbers = list(range(1, 11))

print("完整列表：", numbers)
print("前三个：", numbers[:3])
print("后三个：", numbers[-3:])
print("偶数索引：", numbers[::2])
print("反转：", numbers[::-1])
