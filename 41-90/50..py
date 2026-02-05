#将列表分成指定大小的块

n = int(input("请输入列表元素的个数："))
list1 = []
for i in range(1, n+1):
    message = input("请输入第{}个元素：".format(i))
    list1.append(message)

k = int(input("请输入每个块的大小："))
list2 = [list1[i:i+k] for i in range(0, n, k)]
print("分块后的列表为：", list2)
