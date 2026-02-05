#猴子每天吃一半加一个，第10天生一个，求第1天总数
peach = 1

for day in range(9, 0, -1):
    peach = (peach + 1) * 2 

print(f"第1天的桃子总数是：{peach}个")