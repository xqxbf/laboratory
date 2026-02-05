from collections import Counter
#统计列表中个元素出现次数
list1 = []
n = int(input("请输入列表元素个数："))
for i in range(n):
    num = int(input("请输入第{}个元素：".format(i+1)))
    list1.append(num)

# 使用Counter统计列表中各元素出现次数
count = Counter(list1)
for element, freq in count.items():
    print(f"元素 {element} 出现 {freq} 次")
