# 多种字符串格式化方法比较

name = input("请输入姓名：")
age = int(input("请输入年龄："))

# 百分号（%）格式化
print("hello %s, you are %d years old." % (name, age))

# 格式化字符串（f-string）
print(f"hello {name}, you are {age} years old.")

# str.format() 方法
print("hello {}, you are {} years old.".format(name, age))

# 字符串拼接
print("hello " + name + ", you are " + str(age) + " years old.")

# str.join() 方法
print("hello " + " and ".join([name, "friend"]) + ", you are " + str(age) + " years old.")