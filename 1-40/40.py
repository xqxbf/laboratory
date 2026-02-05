#2/1+3/2+5/3+8/5+...前20项和
sum = 0
a = 2
b = 1
for i in range(1, 21):
    sum += a / b
    a, b = b, a + b
print(f"前20项和为：{sum}")
