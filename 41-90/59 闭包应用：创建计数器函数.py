#闭包应用：创建计数器函数

def create_counter(initial = 0):
    count = initial
    def counter():
        #计数器函数，每次调用增加1，并返回
        nonlocal count 
        count += 1
        return count
    return counter #返回内部函数counter

counter1 = create_counter()

print('第一次调用counter1返回:', counter1())
print('第二次调用counter1返回:', counter1())
print('第三次调用counter1返回:', counter1())
