#将列表元素向右旋转k个位置

list1 = []
for i in range(1, n+1):
    message = input("请输入第{}个元素：".format(i))
    list1.append(message)
    
k = int(input("请输入旋转的位置数："))
list1 = list1[-k:] + list1[:-k]
print("旋转后的列表为：", list1)

 

 
