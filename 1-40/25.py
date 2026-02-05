#根据输入打印对应大小的菱形
rows = int(input("请输入层数："))

if rows % 2 == 0:
    n = int(rows / 2)
else :
    n = int((rows + 1) / 2)

for i in range(n):
    print(" " * (n - i - 1), end='')
    print("*" * (2 * i + 1))
for i in reversed(range(n - 1)):
    print(" " * (n - i - 1), end='')
    print("*" * (2 * i + 1))