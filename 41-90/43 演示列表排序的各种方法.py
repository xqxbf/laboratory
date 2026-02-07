#演示列表排序的各种方法
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

#临时排序
print("临时升序：", sorted(numbers))
print("临时降序：", sorted(numbers, reverse=True))

#永久排序
numbers.sort()
print("永久升序：", numbers)
numbers.sort(reverse=True)
print("永久降序：", numbers)

#自定义排序
words = ['apple', 'Banana', 'cherry', 'Date']
words.sort(key=str.lower)
print("忽略大小写排序：", words)

