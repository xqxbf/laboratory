#演示列表的增删改查
fruits = ['apple', 'banana', 'cherry']

#增
fruits.append('orange') #末尾添加
fruits.insert(1, 'grape') #指定位置插入

#删
removed = fruits.pop(2) #删除并返回第三个元素
fruits.remove('banana') #删除指定元素

#改
fruits[0] = 'peach'

#查
if 'orange' in fruits:
    print("orange在列表中")
else:
    print("orange不在列表中")